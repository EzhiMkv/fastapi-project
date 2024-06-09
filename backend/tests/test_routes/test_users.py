def test_create_user(client):
    data = {"email": "testemail@pew.ru", "password": "testpass"}
    response = client.post("/users", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "testemail@pew.ru"
    assert response.json()["is_active"] == True