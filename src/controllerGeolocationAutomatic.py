import requests

from settings import GOOGLE_MAPS_API_KEY

GOOGLE_MAPS_GEOCODING_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


async def quality_google(quality):
    if quality == 'ROOFTOP':
        quality_spanish = "Ubicación exacta"
    elif quality in ('RANGE_INTERPOLATED', 'GEOMETRIC_CENTER', 'APPROXIMATE'):
        quality_spanish = "Ubicación aproximada"
    else:
        quality_spanish = "Dirección no encontrada."
    return quality_spanish


async def geolocation_google(all_address):
    """
    Args:
        all_address(dict): Contains all the data for an address
    Returns:
        (dict)
    """
    request_params = {'key': GOOGLE_MAPS_API_KEY,
                      'address': " ".join(filter(None, list(all_address.values())[0:6])),
                      'components': f"country:{all_address['country']}" if all_address["country"] else "Mexico"}

    geocoding_response = requests.get(GOOGLE_MAPS_GEOCODING_URL, params=request_params).json()
    # Valid if results found
    if geocoding_response.get("status") != "OK":
        return {"latitude": 'Null', "longitude": 'Null', "quality": "Dirección no encontrada."}
    # Validate that there is only one result
    if len(geocoding_response.get("results")) != 1:
        return {"latitude": 'Null', "longitude": 'Null', "quality": "Se encontró más de una dirección"}
    location = geocoding_response.get("results")[0]
    # Validate the quality of the geolocation
    if location.get("types")[0] in ['route', 'street_address', 'subpremise', 'premise']:
        geometry = location.get("geometry")
        coordinates = geometry.get("location")
        latitude = coordinates.get("lat")
        longitude = coordinates.get("lng")
        quality = await quality_google((geometry.get("location_type", {})).upper())
        return {"latitude": latitude, "longitude": longitude, "quality": quality}
    else:
        return {"latitude": 'Null', "longitude": 'Null', "quality": "Dirección incompleta"}


async def response(geolocation):
    return {
        "coords": {
            "latitude": geolocation["latitude"],
            "longitude": geolocation["longitude"]
        },
        "quality": geolocation["quality"]
    }
