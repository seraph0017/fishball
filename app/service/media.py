#!/usr/bin/env python
# encoding:utf-8

import configs
import datetime

from os import path
from app.misc.public import to_chinese

from app.sqls.media import Medias
from devtools import debug
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


def get_medias(skip: int = 0, limit: int = 12):
    return (
        db.session.query(Medias)
        .filter(Medias.is_active == True)
        .order_by(Medias.update_time.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_total_medias():
    return db.session.query(Medias).filter(Medias.is_active == True).count()

def get_total_page_num():
    total_medias = get_total_medias()
    page_num, other = divmod(total_medias, configs.ONE_PAGE_LIMIT)
    if other != 0:
        page_num += 1
    return page_num


def convert_page_to_skip_limit(page):
    return configs.ONE_PAGE_LIMIT * (page - 1), configs.ONE_PAGE_LIMIT * (page)


def get_media_by_id(media_id):
    return (
        db.session.query(Medias)
        .filter(Medias.id == media_id, Medias.is_active == True)
        .first()
    )


def edit_media(media_id, mediaEdit):
    media = get_media_by_id(media_id)
    media.title = mediaEdit.mediaTitle
    media.description = mediaEdit.mediaDescription
    media.pic_time = mediaEdit.mediaTime
    db.session.add(media)
    db.session.commit()
    db.session.refresh(media)
    return media


def parse_media_recent(medias):
    for media in medias:
        td = datetime.datetime.now() - media.update_time
        d = td.days
        totalMin, s = divmod(td.seconds, 60)
        h, m = divmod(totalMin, 60)
        yield media, d, h, m, s


def count_age():
    today = datetime.date.today()
    f_age, _ = divmod((today - configs.F_BIRTHDAY).days, 365.25)
    c_age, _ = divmod((today - configs.C_BIRTHDAY).days, 365.25)
    return to_chinese(int(f_age)), to_chinese(int(c_age))
