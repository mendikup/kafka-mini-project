from fastapi import FastAPI
from manager import Manager
from helpers import convert_bson_types


app = FastAPI()
manager = Manager()

@app.get("/consume")
def consume():
    return manager.get_consume()

@app.get("/all_data")
def get_all_data():

    return convert_bson_types(manager.get_all_data())


if __name__=="__main__":
    uvicorn.run("subscribe_not_interesting.main:app", host="0.0.0.0", port=8003)