import uvicorn
from fastapi import FastAPI




app = FastAPI()


@app.get("/")
def root():
    return {"status": "pub server is ok"}


@app.get("/publish")
def publish():
    pass

if __name__=="__main__":
    uvicorn.run("publisher.main:app", host="0.0.0.0", port=8001)