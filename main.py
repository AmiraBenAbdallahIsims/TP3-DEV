from fastapi import FastAPI

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
