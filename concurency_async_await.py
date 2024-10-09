from typing import Union
from fastapi import FastAPI

app = FastAPI()
# results = await some_library()

# @app.get('/')
# async def read_results():
#     results = await some_library()
#     return results

# @app.get('/')
# def results():
#     results = some_library()
#     return results

# burgers = await get_bergers(2)

# async def get_burgers(number: int):
#     # Do some asynchronous stuff to create the burgers
#     return burgers
# 
# instead of def:
# 
# def get_sequential_burgers(number: int):
#     # Do some sequential stuf to create the burgers
#     return burgers

# This won't work, because get_burgers was defined with: async def
# burgers = get_burgers(2)

# @app.get('/burgers')
# async def read_burgers():
#     burgers = await get_burgers(2)
#     return burgers