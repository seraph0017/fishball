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
    return (
        db.session.query(Users)
        .filter(Users.email == user_email, Users.is_active == True)
        .first()
    )

def user_load_query_by_email(user_email: str):
    with db():
        user = db.session.query(Users).filter(Users.email == user_email, Users.is_active == True).first()
    return user


def create_user(user):
    u = Users(**user)
    db.session.add(u)
    db.session.commit()
    db.session.refresh()
    return u