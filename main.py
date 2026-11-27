from fastapi import FastAPI
from pydantic import BaseModel
import socket
app = FastAPI()


@app.get("/")
def accueil():
    return {"message": "Hello World"}

@app.get("/addition")
def addition(a: int, b: int):
    return {
        "result": a + b,
        "developer": "Dev1"
    }
@app.get("/greeting")
def greeting(name: str):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "ip": ip
    }

    
class Operation(BaseModel):
    a: float
    b: float


@app.post("/multiply")
def multiply(operation: Operation):
    return {
        "result": operation.a * operation.b,
        "developer": "Dev1"
    }
@app.get("/soustraction")
def soustraction(a: float, b: float):
    return {"result": a - b}