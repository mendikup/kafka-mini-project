import uvicorn
from fastapi import FastAPI
from manager import Manager




app = FastAPI()
manager = Manager()


@app.get("/")
def root():
    return {"status": "pub server is running"}


@app.get("/publish")
def publish():
    manager.run()
    return {"status":"succeeded"}


if __name__ == "__main__":
    uvicorn.run("components.publisher.main:app", host="0.0.0.0", port=8001)
