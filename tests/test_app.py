from flask.testing import FlaskClient

def test_add_path(client : FlaskClient, app):
    new_path = [
        {
            "SH": 56,
            "distance": 32
        }, 
        {
            "SH": 1016,
            "distance": 44
        },
        {
            "SH": 24,
            "distance": 49
        }
    ]
    response = client.post("/api/add_path", json=new_path)
    assert response.status_code == 200
    assert app.config["CURRENT_PATHS"][-1] == new_path

    new_path = []
    response = client.post("/api/add_path", json=new_path)
    assert response.status_code == 400

def test_cals(client : FlaskClient, app):
    parameters = {
        "i": 1
    }
    response = client.get("/api/calcs", query_string = parameters)
    assert response.status_code == 200

    parameters = {
        "i": 8
    }
    response = client.get("/api/calcs", query_string = parameters)
    assert response.status_code == 400

    parameters = {
        "i": None
    }
    response = client.get("/api/calcs", query_string = parameters)
    assert response.status_code == 400