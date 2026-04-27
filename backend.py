from fastapi import FastAPI
from pydantic import BaseModel
from main_logic import enrich_company

app = FastAPI()
store = []

class URLRequest(BaseModel):
    url: str

@app.post("/enrich")
def enrich(req: URLRequest):
    data = enrich_company(req.url)
    store.append(data)
    return data

@app.get("/results")
def results():
    return store
