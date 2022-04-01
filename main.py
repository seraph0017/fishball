#/usr/bin/env python
#encoding:utf-8

from urllib import request
import configs

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory=configs.TEMPLATE_FILES_PATH)

app = FastAPI()


app.mount("/statics", StaticFiles(directory=configs.STATIC_FILES_PATH),name="static")


@app.get("/")
async def indexl_handle(request: Request):
    return templates.TemplateResponse("_base.html", {"request":request})



@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return dict(item_id=item_id)

