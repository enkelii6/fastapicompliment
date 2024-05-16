from typing import Annotated
from fastapi import FastAPI, Form, Request
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='static')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse("createpage.html", {'request': request})

@app.get('/show')
async def main(request: Request, sex: str, name: str):
    if sex == "m":
        responce = requests.get('https://tools-api.robolatoriya.com/compliment?type=3')
    elif sex == "f":
        responce = requests.get('https://tools-api.robolatoriya.com/compliment?type=2')
    else:
        responce = requests.get('https://tools-api.robolatoriya.com/compliment?type=1')
    return templates.TemplateResponse("index.html", {'request': request, 'sex': sex, 'name': name, 'compliment': responce.json()['text']})

