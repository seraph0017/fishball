#!/usr/bin/env python
#encoding:utf-8
from app.sqls.photo import Photo


class PhotoService(object):
    pass




def upload_photo(db, photoform):
    upload_file = photoform.upload_file
    photo_dict = photoform.dict()
    photo_dict.pop("upload_file")
    photo = Photo(**photo_dict)
    db.session.add(photo)
    db.session.commit()
    db.session.refresh(photo)
    return photo
