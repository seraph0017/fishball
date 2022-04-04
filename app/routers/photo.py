#!/usr/bin/env python
# encoding:utf-8

import configs
from os import path
from typing import List

from app.misc.public import templates
from fastapi import APIRouter, Request, UploadFile
from fastapi_sqlalchemy import db

from app.sqls.photo import Photo
from app.schmas.photo import PhotoCreateSchema

from app.service.photo import upload_photo


from devtools import debug
from app.logger import logger as l


photo_router = APIRouter(prefix="/photos", tags=["photos"])

tp_url_list = [
    "WechatIMG3589.jpeg",
    "WechatIMG3590.jpeg",
    "WechatIMG3591.jpeg",
    "WechatIMG3592.jpeg",
    "WechatIMG3593.jpeg",
    "WechatIMG3594.jpeg",
    "WechatIMG3595.jpeg",
    "WechatIMG3596.jpeg",
    "WechatIMG3597.jpeg",
    "WechatIMG3598.jpeg",
]


@photo_router.get("/", name="photo_index")
def photo_index_handle(request: Request):
    re_context = dict(
        request=request,
        url_list=tp_url_list,
        title="鱼丸札记",
        project_name="鱼丸札记",
    )
    return templates.TemplateResponse("photo/photo_base.jinja2", re_context)


@photo_router.post("/", name="photo_add")
async def photo_add_handle(request: Request, mediafiles: List[UploadFile]):
    for mediafile in mediafiles:
        l.debug(mediafile.filename)
        contents = await mediafile.read()
        with open(path.join(configs.UPLOADS_FILES_PATH, mediafile.filename), 'wb+') as f:
            f.write(contents)
    return {'filenames': [file.filename for file in mediafiles]}




@photo_router.put("/", name="photo_msg_edit")
async def photo_msg_edit_handle(request: Request, photo: PhotoCreateSchema):
    debug(photo)
    l.debug(photo)
    return upload_photo(db, photo)