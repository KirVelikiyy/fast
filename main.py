from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Fruits(Enum):
    apple = "apple"
    banana = "banana"
    strawberry = "strawberry"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/fruits/{fruit}")
async def get_fruit(fruit: Fruits):
    default_message = "Your fruit is"
    match fruit:
        case Fruits.apple:
            return {"message": f"{default_message} {Fruits.apple.value}"}
        case Fruits.banana:
            return {"message": f"{default_message} {Fruits.banana.value}"}
        case Fruits.strawberry:
            return {"message": f"{default_message} {Fruits.strawberry.value}"}
