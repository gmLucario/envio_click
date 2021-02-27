from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_vowels_post_expected_code():
    response = client.post("/vowels/", json={"line": "HOLA"})

    assert response.status_code == 200


def test_vowels_post_result():
    response = client.post("/vowels/", json={"line": "HOLA"})
    assert response.json() == {
        "data": {"vowels_count": 2, "new_line": "HULE"},
        "message": "success",
        "code": 200,
    }
