from fastapi.testclient import TestClient
from main import app


def test_geocoding_ok():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={'street': 'C.Costa Rica', 'postal_code': 93320})
    assert response.status_code == 200


def test_geocoding_no_street():
    client = TestClient(app)
    response = client.get(
        url='/geolocation')
    assert response.status_code == 422


def test_geocoding_params_vacios():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={"street": 'vacio', "number": 'vacio', "district": 'vacio',
                "postal_code": 'vacio', "city": 'vacio', "state": 'vacio', "country": 'vacio'})
    assert response.json().get('quality') == 'Dirección incompleta'


def test_geocoding_sn():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={'street': 'C.Costa Rica', "number": 's/n', 'postal_code': 93320})
    assert response.status_code == 200


def test_geocoding_street_district():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={'street': 'C.Costa Rica', 'district': '27 de septiembre'})
    assert response.status_code == 200


def test_gecoding_country():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={'street': 'C.Costa Rica'})
    assert response.status_code == 200


def test_gecoding_state():
    client = TestClient(app)
    response = client.get(
        url='/geolocation',
        params={'street': 'C.Costa Rica', 'state': 'Veracruz'})
    assert response.json().get('quality') == 'Dirección incompleta'