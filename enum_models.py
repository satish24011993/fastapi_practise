from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    data2 = 'data3'

app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name':model_name, 'message':'alexnet viewed! and Deep Learning FTW!'}
    
    if model_name.value == 'lenet':
        return {'model_name':model_name, 'message':'LeCNN all the images'}
    
    # if model_name is ModelName.data2:
    #     return {'model_name':model_name, 'message':'data2 got viewed'}
    
    return {'model_name':model_name, 'message':'Have some residuals'}

@app.get('/models')
async def all_models():
    return ModelName


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path':file_path}