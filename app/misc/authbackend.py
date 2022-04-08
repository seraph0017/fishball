#!/usr/bin/env python
# encoding:utf-8

import aioredis
import configs


from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    RedisStrategy,
)

from app.schmas.user import UserCreate
from app.sqls.user import UserDB


cookie_transport = CookieTransport(cookie_max_age=60 * 60)

redis = aioredis.from_url(configs.REDIS_URI, decode_response=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=60 * 60)


auth_backend = AuthenticationBackend(
    name="cr_auth",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)
