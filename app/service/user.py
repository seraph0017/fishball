#!/usr/bin/env python
# encoding:utf-8


from app.sqls.user import Users


from fastapi_sqlalchemy import db

from devtools import debug


def query_user_by_id(user_id: int):
    return (
        db.session.query(Users)
        .filter(Users.id == user_id, Users.is_active == True)
        .first()
    )


def query_user_by_email(user_email: str):
    debug(user_email)
    user = (
        db.session.query(Users)
        .filter(Users.email == user_email, Users.is_active == True)
        .first()
    )
    debug(user)
    return user


def user_load_query_by_email(user_email: str):
    with db():
        user = (
            db.session.query(Users)
            .filter(Users.email == user_email, Users.is_active == True)
            .first()
        )
    return user


def create_user(user):
    u = Users(**user.dict())
    db.session.add(u)
    db.session.commit()
    db.session.refresh(u)
    return u

def update_user_by_id(user_id, user_update):
    u = db.session.query(Users).filter(Users.id == user_id).first()
    u.email = user_update.email
    u.hashed_password = user_update.hashed_password
    u.nick_name = user_update.nick_name
    u.user_type = user_update.user_type
    u.is_active = user_update.is_active
    u.is_superuser = user_update.is_superuser
    db.session.add(u)
    db.session.commit()
    db.session.refresh(u)
    return u


def get_all_user():
    return db.session.query(Users).all()


def get_user_by_id(user_id: int):
    return db.session.query(Users).filter(Users.id == user_id).first()


def get_user_count():
    return db.session.query(Users).count()
