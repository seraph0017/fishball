#!/usr/bin/env python
# encoding:utf-8

import configs

from os import path

from app.sqls.media import Medias
from fastapi_sqlalchemy import db


class PhotoService(object):
    pass


def upload_media(user_id, filename, contents):
    ext_file_name = ""
    is_pic = True
    upload_filepath = path.join(configs.UPLOADS_FILES_PATH, filename)
    with open(upload_filepath, "wb+") as f:
        f.write(contents)
    if filename != "":
        ext_file_name = filename.split(".")[-1:].pop()
    if ext_file_name not in ["jpeg", "png", "jpg"]:
        is_pic = False
    media = Medias(
        upload_local_file_path=upload_filepath,
        upload_user_id=user_id,
        upload_render_file_path=filename,
        is_pic=is_pic,
    )
    db.session.add(media)
    db.session.commit()
    db.session.refresh(media)
    return media


def get_medias(skip: int = 0, limit: int = 10):
    return db.session.query(Medias).order_by(Medias.update_time.desc()).offset(skip).limit(10).all()
