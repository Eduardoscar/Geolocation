from fastapi import FastAPI, status, responses

import geolocationAutomatic

app = FastAPI()


@app.get("/geolocation")
async def root(street: str, number: str = None, district: str = None,
               postal_code: str = None, city: str = None, state: str = None,
               country: str = 'Mexico'):
    address = {"street": street, "number": number, "district": district,
               "postal_code": postal_code, "city": city, "state": state, "country": country}
    response = await geolocationAutomatic.coords(address, 'GOOGLE')
    return responses.JSONResponse(content=response, status_code=status.HTTP_200_OK)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
