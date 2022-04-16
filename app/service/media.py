#!/usr/bin/env python
# encoding:utf-8

from re import I
from app.sqls import user
import configs
import datetime

from os import path, mkdir
from pathlib import Path

from app.misc.public import to_chinese

from app.sqls.media import Medias, MediaGroups
from devtools import debug
from fastapi_sqlalchemy import db


class MediaService(object):
    pass


def upload_media(user_id, media_group_id, filename, contents):
    ext_file_name = ""
    is_pic = True
    if not Path(path.join(configs.UPLOADS_FILES_PATH, str(media_group_id))).exists():
        mkdir(path.join(configs.UPLOADS_FILES_PATH, str(media_group_id)))
    upload_filepath = path.join(
        configs.UPLOADS_FILES_PATH, str(media_group_id), filename
    )
    debug(upload_filepath)
    with open(upload_filepath, "wb+") as f:
        f.write(contents)
    if filename != "":
        ext_file_name = filename.split(".")[-1:].pop()
    if ext_file_name not in ["jpeg", "png", "jpg", "JPG"]:
        is_pic = False
    media = Medias(
        upload_local_file_path=upload_filepath,
        upload_user_id=user_id,
        upload_render_file_path=path.join(str(media_group_id), filename),
        is_pic=is_pic,
        group_id=media_group_id,
    )
    db.session.add(media)
    db.session.commit()
    db.session.refresh(media)
    return media


def get_medias(media_group_id: int = 1, skip: int = 0, limit: int = 12):
    return (
        db.session.query(Medias)
        .filter(Medias.is_active == True, Medias.group_id == media_group_id)
        .order_by(Medias.pic_time.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_total_medias(media_group_id):
    return (
        db.session.query(Medias)
        .filter(Medias.is_active == True, Medias.group_id == media_group_id)
        .count()
    )


def get_total_page_num(media_group_id):
    total_medias = get_total_medias(media_group_id)
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


def create_media_group(mediagroup):
    mg = MediaGroups(**mediagroup.dict())
    db.session.add(mg)
    db.session.commit()
    db.session.refresh(mg)
    return mg

def update_media_group_by_id(media_group_id, media_group_update):
    mg = db.session.query(MediaGroups).filter(MediaGroups.id == media_group_id).first()
    mg.title = media_group_update.title
    mg.description = media_group_update.description
    mg.is_active = media_group_update.is_active
    mg.group_level = media_group_update.group_level
    db.session.add(mg)
    db.session.commit()
    db.session.refresh(mg)
    return mg

def get_media_groups_by_user_type(user_type):
    return (
        db.session.query(MediaGroups)
        .filter(
            MediaGroups.is_active == True,
            MediaGroups.group_level >= user_type,
        )
        .all()
    )


def get_media_group_by_id(id):
    return db.session.query(MediaGroups).filter(MediaGroups.id == id).first()


def get_media_count():
    return db.session.query(Medias).count()


def get_media_group_count():
    return db.session.query(MediaGroups).count()


def get_all_media_group():
    return db.session.query(MediaGroups).all()

