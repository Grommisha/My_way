from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title='my application')

users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
]

trades = [
    {'id': 1, 'user_id': 1, 'side': 'buy'},
    {'id': 2, 'user_id': 1, 'side': 'sell'},
]


class Trade(BaseModel):
    id: int
    user_id: int = Field(ge=0)
    side: str


class User(BaseModel):
    id: int
    role: str
    name: str


@app.post('/trades')
def add_trades(trade: List[Trade]):
    trades.extend(trade)
    return {'status': 200, 'data': trades}


@app.get("/users/{user_id}", response_model=List[User])
def hello(user_id: int):
    return [user for user in users if user.get("id") == user_id]

@app.post("/users")
def change_name(user_id: int, name: str):
    current_users = list(filter(lambda user: user.get('id') == user_id, users))
    for user in current_users:
        user['name'] = name
    return {'status': 200, 'data': current_users}

