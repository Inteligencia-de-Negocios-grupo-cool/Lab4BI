from typing import Optional
from joblib import load
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from DataModel import DataModelapp

app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}



