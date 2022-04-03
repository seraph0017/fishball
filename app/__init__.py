#!/usr/bin/env python
# encoding:utf-8
import configs

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_sqlalchemy import DBSessionMiddleware


from starlette.responses import RedirectResponse

from app.routers import photo
from app.misc.public import templates


app = FastAPI()

app.include_router(photo.photo_router)

app.mount("/statics", StaticFiles(directory=configs.STATIC_FILES_PATH), name="static")
app.mount("/upload", StaticFiles(directory=configs.UPLOADS_FILES_PATH), name="upload")

app.add_middleware(DBSessionMiddleware, db_url=configs.DATABASE_URI)


@app.get("/", name="index_handle")
def index_handle(request: Request):
    return RedirectResponse(url=app.url_path_for("photo_index"))
