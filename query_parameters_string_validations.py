from typing import Union

from fastapi import FastAPI,Query
from typing_extensions import Annotated

app = FastAPI()


# @app.get('/items/')
# async def read_items(q: Union[str, None] = None):
#     results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
#     if q:
#         results.update({'q':q})
#     return results

@app.get('/items/')
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)]=None):
    results = {'items': [{'item_id':'Foo'}, {'item_id':'Bar'}]}

    if q:
        results.update({'q':q})
    return results


@app.get('/items_name/')
async def read_items(q: Annotated[str, Query()]='rick'):
    results = {'items': [{'item_id':'Foo'}, {'item_id':'Bar'}]}

    if q:
        results.update({'q':q})
    return results

# Python 3.10+
# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

@app.get('/items_val/')
async def read_items(
    q: Annotated[Union[str, None], Query(min_length=3, max_length=50)] = None,
):
    results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results

# Regular expressions
@app.get('/items_fixed/')
async def read_items(
    q: Annotated[
        Union[str, None], Query(min_length=3, max_length=50, pattern='^fixedquery$')
    ] = None,
):
    results = {'items':[{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results


@app.get('/items_regex/')
async def read_items(
    q: Annotated[
        Union[str, None], Query(min_length=3, max_length=50, regex='^fixedquery$')
    ] = None,
):
    results = {'items':[{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results


# annotated to default values
@app.get('/items_default/')
async def read_items(
    q: Annotated[str, Query(min_length=3)] = 'fixedquery'
):
    results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results


@app.get('/items_ann/')
async def read_items(q: Annotated[str, Query(min_length=3)]=None):
    results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results


@app.get('/items_ellipsis/')
async def read_items(q: Annotated[str, Query(min_length=2)]= ...):
    results = {'items': [{'item_id':'Foo'}, {'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results

# Required can be null
@app.get('/items_none/')
async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
    results = {'items': [{'item_id':'Foo'},{'item_id':'Bar'}]}
    if q:
        results.update({'q':q})
    return results