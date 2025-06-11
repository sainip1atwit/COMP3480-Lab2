from fastapi.testclient import TestClient
from Lab2 import app

client = TestClient(app)

def test_get_user_agent():
    response = client.get("/user_agent")
    assert response.status_code == 200
    assert response.json() == { "User-Agent": "testclient" }

def test_age_headers():
    headers = { "age": "22" }
    response = client.get("/age_headers", headers=headers)
    assert response.status_code == 200
    assert response.json() == { "age": 22 }

def test_calculate_headers():
    headers = {
        "num1": "12",
        "num2": "10",
        "operation": "add"
    }
    response = client.get("/calculate_headers", headers=headers)
    assert response.status_code == 200
    assert response.json() == { "answer": "12 + 10 = 22" }

def test_play_rps_headers():
    headers = { "choice": "rock" }
    results = [
        { "result": "Computer chose ROCK, draw!" },
        { "result": "Computer chose PAPER, you lose!" },
        { "result": "Computer chose SCISSORS, you win!" }]
    response = client.get("/play_rps_headers", headers=headers)
    assert response.status_code == 200
    assert response.json() in results

def test_age_cookies():
    cookies = { "age": "22" }
    response = client.post("/age_cookies", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == { "age": "22" }

def test_calculate_cookies():
    cookies = {
        "num1": "12",
        "num2": "10",
        "operation": "add"
    }
    response = client.post("/calculate_cookies", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == { "answer": "12 + 10 = 22" }

def test_play_rps_cookies():
    cookies = { "choice": "rock" }
    results = [
        { "result": "Computer chose ROCK, draw!" },
        { "result": "Computer chose PAPER, you lose!" },
        { "result": "Computer chose SCISSORS, you win!" }]
    response = client.post("/play_rps_cookies", cookies=cookies)
    assert response.status_code == 200
    assert response.json() in results