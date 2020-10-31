import requests

def test_get1_check():
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1&id=1&email=Eliseo@gardner.biz")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    response_body = response.json()
    assert response_body[0]["postId"] == 1
    assert response_body[0]['id'] == 1
    assert response_body[0]["name"] == "id labore ex et quam laborum"
    assert response_body[0]["email"] == "Eliseo@gardner.biz"
    assert response_body[0]["body"] == "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"

def test_get2_check():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/5?userid=1")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    response_body = response.json()
    assert response_body['userId'] == 1
    assert response_body['id'] == 5

def test_get3_check():
    response = requests.get("https://jsonplaceholder.typicode.com/users?id=26")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    response_body = response.json()
    assert response_body[0]["id"] == 26

