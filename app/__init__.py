#!/usr/bin/env python
#encoding:utf-8
import configs

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from app.routers import photo

from app.misc.public import templates



app = FastAPI()

app.include_router(photo.photo_router)
app.mount("/statics", StaticFiles(directory=configs.STATIC_FILES_PATH),name="static")
app.mount("/photos/statics", StaticFiles(directory=configs.STATIC_FILES_PATH),name="static")


@app.get("/")
def index_handle(request: Request):
    return templates.TemplateResponse("_base.html", {"request":request})


