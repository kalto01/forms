from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_form_types():
    response = client.post(
        "/get_form",
        json={
          "fields": {
            "user name": "asd@as.ru",
            "bb": "7123123",
            "date order": "2021-12-01",
            "date end": "01.02.2022",
            "phone": "+71234567891"
          }
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "user name": "email",
            "bb": "text",
            "date order": "date",
            "date end": "date",
            "phone": "phone"
        }
    }


def test_get_form_template_name():
    response = client.post(
        "/get_form",
        json={
            "fields": {
                "user name": "John",
                "lead email": "ass@asd.ru"
            }
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "template_name": "Lead form"
        }
    }
