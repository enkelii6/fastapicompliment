from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

templates = Jinja2Templates(directory='static')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def main(request: Request):
    responce = requests.get('https://tools-api.robolatoriya.com/compliment?type=2')
    return templates.TemplateResponse("index.html", {'request': request, 'compliment': responce.json()['text']})
