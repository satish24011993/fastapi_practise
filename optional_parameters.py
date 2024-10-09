from typing import Union
from fastapi import FastAPI

app = FastAPI()

# @app.get('/items/{item_id}')
# async def read_item(item_id:str, q: Union[str, None]=None):
#     if q:
#         return {'item_id': item_id, 'q':q}
#     return {'item_id':item_id}

@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Union[str, None]=None, short: bool=False):
    item = {'item_id': item_id}
    if q:
        item.update({'q':q})
    if not short:
        item.update(
            {'description':'This is an amazing item that has a long description'}
        )
    return item


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None]=None,short:bool=False
):
    item = {'item_id':item_id, 'owner_id':user_id}
    if q:
        item.update({'q':q})
    if not short:
        item.update(
            {'description':'This is an amazing item that has a long description'}
        )
    return item