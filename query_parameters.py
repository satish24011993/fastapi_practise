from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name':'Foo'},{'item_name': 'Bar'}, {'item_name':'Baz'}]

@app.get('/items/')
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip:skip + limit]


# @app.get('/items/{item_id}')
# async def read_user_item(item_id: str, needy:str):
#     item = {'item_id':item_id, 'needy': needy}
#     return item


@app.get('/items/{item_id}')
async def read_user_item(
    item_id: str, needy: str, skip: int =0, limit: Union[int, None] = None
):
    item = {'item_id': item_id, 'needy': needy, 'skip':skip, 'limit':limit}
    return item