from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'Hello World'}


# differenct operations
# @app.post()
# @app.put()
# @app.delete()

# and more exotic ones:

# @app.options()
# @app.head()
# @app.patch()
# @app.trace()

# @app.get('/items/{item_id}')
# async def read_item(item_id):
#     return {'item_id':item_id}

@app.get('/items/{item_id}')
async def root(item_id: int):
    return {'item_id':item_id}

@app.get('/users/me')
async def read_user_me():
    return {'user_id':'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id:str):
    return {'user_id':user_id}

@app.get('/users')
async def read_users():
    return ['Rick', 'Morty']

@app.get('/users2')
async def read_users2():
    return ['Mr','Bean']

