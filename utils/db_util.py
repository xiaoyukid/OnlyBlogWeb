#!/usr/bin/env python
#coding=utf-8
from configs import settings

__author__ = 'Administrator'
'''
数据库连接
'''

import redis


class DBUtil:
    r = None

    def __init__(self):
        self.r = redis.Redis(host=settings.HOST, port=settings.PORT, db=settings.DB)