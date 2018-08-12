# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

LOGIN_SESSION_SAVE_TIME = 3600 * 2

URL_ENDPOINT = [
    {
        # 学生
        "HOME_URL": "/xs_main.aspx?xh=",
        "SCORE_URL": "/xscj_gc.aspx?xh=",
        "INFO_URL": "/xsgrxx.aspx?gnmkdm=N121501&xh=",
        "SCHEDULE_URL": [
            "/xskbcx.aspx?gnmkdm=N121603&xh=",
            "/tjkbcx.aspx?gnmkdm=N121601&xh=",
        ],
    },
    {
        # 教师
        "HOME_URL": "/js_main.aspx?xh=08020",
        "INFO_URL": "/lw_jsxx.aspx?gnmkdm=N122502&zgh=",
        "SCHEDULE_URL": ["", "/jstjkbcx.aspx?gnmkdm=N122303&zgh="],
    },
    {
        # 部门
        "HOME_URL": "/bm_main.aspx?xh=",
        "SCHEDULE_URL": ["", "/tjkbcx.aspx?gnmkdm=N120313&xh="],
        "PLACE_SCHEDULE_URL": "/kbcx_jxcd.aspx?gnmkdm=N120314&xh=",
    },
]


CLASS_TIME_LIST = {
    # 连续上一节课
    1: [
        "8:30 ~ 9:15",
        "10:25 ~ 11:10",
        "14:40 ~ 15:25",
        "16:30 ~ 17:15",
        "19:30 ~ 20:30",
    ],
    # 连续上两节课
    2: [
        "8:30 ~ 10:05",
        "10:25 ~ 12:00",
        "14:40 ~ 16:15",
        "16:30 ~ 18:05",
        "19:30 ~ 21:05",
    ],
    # 连续上三节课
    3: ["8:30 ~ 11:10", "", "14:40 ~ 17:15"],
    # 连续上四节课
    4: ["8:30 ~ 12:00", "10:25 ~ 16:15", "14:40 ~ 18:05", "16:30 ~ 21:05"],
}