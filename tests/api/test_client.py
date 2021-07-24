from fastapi.testclient import TestClient


def test_successful_get_products(client: TestClient):
    ok_json_client = {
        "data": {
            "name": "Vitya2222",
            "phone": '44444444',
            "email": "vitek_16@prival.ru"
        }
    }

    response = client.post('/api/v1/client', json=ok_json_client)
    assert response.status_code == 201
    # fix id here to actual corresponding db last client index
    assert response.json() == {'client_id': 1}

    response = client.get('/api/v1/client/1')
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "name": "Vitya2222",
            "surname": "",
            "phone": '44444444',
            "email": "vitek_16@prival.ru",
            "client_id": 1
        }
    }
