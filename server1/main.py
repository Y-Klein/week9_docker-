import json

from fastapi import FastAPI


app  = FastAPI()

DB_PATH = "./db/ shopping_list.json"
def load():
    try:
        with open(f"{DB_PATH}", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")

@app.get("/items")
def get_all_items():
    return load()



@app.post("/items")
def add_item(item):
    file = load()
    file["item"].append(item)
    file = str(file)
    with open(f"{DB_PATH}","w") as f :
        f.write(file)

add_item({ "id": 2,"name": "Milk","quantity": 8})
