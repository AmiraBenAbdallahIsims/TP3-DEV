
"""Tests unitaires des routes de l'application FastAPI."""

from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_accueil():
    """Vérifie la route d'accueil."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_addition():
    """Vérifie l'addition de deux nombres."""
    response = client.get("/addition?a=10&b=5")

    assert response.status_code == 200
    assert response.json() == {
        "result": 15,
        "developer": "Dev1"
    }


def test_greeting(monkeypatch):
    """Vérifie le message et les informations du serveur."""
    monkeypatch.setattr(
        main.socket,
        "gethostname",
        lambda: "test-host"
    )
    monkeypatch.setattr(
        main.socket,
        "gethostbyname",
        lambda hostname: "127.0.0.1"
    )

    response = client.get("/greeting?name=Amira")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Amira",
        "developer": "Dev2",
        "hostname": "test-host",
        "ip": "127.0.0.1"
    }


def test_multiply():
    """Vérifie la multiplication de deux nombres."""
    response = client.post(
        "/multiply",
        json={"a": 5, "b": 4}
    )

    assert response.status_code == 200
    assert response.json() == {
        "result": 20,
        "developer": "Dev1"
    }


def test_soustraction_positifs():
    """Vérifie la soustraction de deux nombres positifs."""
    response = client.get("/soustraction?a=10&b=4")

    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_soustraction_resultat_negatif():
    """Vérifie une soustraction donnant un résultat négatif."""
    response = client.get("/soustraction?a=4&b=10")

    assert response.status_code == 200
    assert response.json() == {"result": -6}


def test_soustraction_nombres_decimaux():
    """Vérifie la soustraction de nombres décimaux."""
    response = client.get("/soustraction?a=10.5&b=2.5")

    assert response.status_code == 200
    assert response.json() == {"result": 8.0}


def test_soustraction_zero():
    """Vérifie la soustraction avec zéro."""
    response = client.get("/soustraction?a=10&b=0")

    assert response.status_code == 200
    assert response.json() == {"result": 10}


def test_soustraction_nombres_egaux():
    """Vérifie la soustraction de deux nombres égaux."""
    response = client.get("/soustraction?a=5&b=5")

    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_soustraction_parametre_manquant():
    """Vérifie la réponse lorsque le paramètre b est absent."""
    response = client.get("/soustraction?a=10")

    assert response.status_code == 422
