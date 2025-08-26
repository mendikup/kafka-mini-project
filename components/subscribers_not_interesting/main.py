import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "not_inserting topic_sub server is ok"}


@app.get("/not_interesting_topics")
def get_not_interesting_topics():
  pass


if __name__=="__main__":
    uvicorn.run("subscribe_not_interesting.main:app", host="0.0.0.0", port=8003)