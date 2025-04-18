from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
class Item(BaseModel):
    name: str
    description: str | None = None


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http://localhost:.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Item {item.name} created"}