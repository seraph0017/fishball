#!/usr/bin/env python
# encoding:utf-8
import configs
from typing import Optional
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory=configs.TEMPLATE_FILES_PATH)


_MAPPING = (
    "零",
    "一",
    "二",
    "三",
    "四",
    "五",
    "六",
    "七",
    "八",
    "九",
    "十",
    "十一",
    "十二",
    "十三",
    "十四",
    "十五",
    "十六",
    "十七",
    "十八",
    "十九",
)
_P0 = (
    "",
    "十",
    "百",
    "千",
)
_S4 = 10**4


def to_chinese(num):
    assert 0 <= num and num < _S4
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = ""

        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += "零"
        return result[::-1]


