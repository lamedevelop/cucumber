from fastapi.testclient import TestClient


def test_successful_get_products(client: TestClient):
    # response = client.post('/products', json=json_products)
    response = client.get('/api/v1/products')
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            {
                "product_id": 1,
                "name": "kolbasa",
                "price": 150.0,
                "category": 1,
                "availability": True
            },
            {
                "product_id": 2,
                "name": "barashek",
                "price": 5000.0,
                "category": 1,
                "availability": True
            },
            {
                "product_id": 3,
                "name": "tort",
                "price": 230.0,
                "category": 2,
                "availability": True
            }
        ]
    }


def test_successful_get_categories(client: TestClient):
    response = client.get('/api/v1/categories')
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            {
                "category_id": 1,
                "name": "meat"
            },
            {
                "category_id": 2,
                "name": "candy",
            }
        ]
    }
