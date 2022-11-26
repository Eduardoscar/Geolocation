import controllerGeolocationAutomatic


async def coords(address, map_provider):
    """
    Args:
        address(dict): Contains all the data for an address
        map_provider(str): Provider of geolocation to use
    Returns:
    """
    # Data cleaning
    for key, valor in address.items():
        if valor:
            if valor.upper() in ["VACIO", "VACIÓ"]:
                address[key] = None
    if address["number"]:
        address["number"] = address["number"].replace('/', '')
    # It is validated if you have the necessary data for a geolocation
    if address["street"] and (address["district"] or address["postal_code"]):
        if map_provider.upper() == 'GOOGLE':
            data = await controllerGeolocationAutomatic.geolocation_google(address)

    else:
        # The quality with null coordinates is added
        data = {"latitude": 'Null', "longitude": 'Null'}
        try:
            address_type = [type(address["street"]), type(address["district"]), type(address["postal_code"]),
                            type(address["city"]), type(address["state"])]
            address_name = ["street", "district", "postal_code", "city", "state"]
            index = address_type.index(str)
            if address_name[index] == "street":
                data["quality"] = "Dirección incompleta"
            else:
                data["quality"] = "Zona demasiada amplia para geolocalizar"
        except:
            data["quality"] = "Dirección incompleta"

    return await controllerGeolocationAutomatic.response(data)

