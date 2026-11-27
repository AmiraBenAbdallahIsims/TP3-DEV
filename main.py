
"""Application FastAPI contenant les opérations mathématiques et les routes HTTP."""

import socket

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def accueil():
    """Retourne un message d'accueil."""
    return {"message": "Hello World"}


@app.get("/addition")
def addition(a: int, b: int):
    """Effectue l'addition de deux nombres entiers."""
    return {
        "result": a + b,
        "developer": "Dev1"
    }


@app.get("/greeting")
def greeting(name: str):
    """Retourne un message personnalisé et les informations du serveur."""
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "ip": ip
    }


class Operation(BaseModel):
    """Représente deux nombres pour une opération mathématique."""

    a: float
    b: float


@app.post("/multiply")
def multiply(operation: Operation):
    """Effectue la multiplication de deux nombres."""
    return {
        "result": operation.a * operation.b,
        "developer": "Dev1"
    }


@app.get("/soustraction")
def soustraction(a: float, b: float):
    """Effectue la soustraction de deux nombres."""
    return {"result": a - b}
