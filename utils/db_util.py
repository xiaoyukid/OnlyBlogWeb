#!/usr/bin/env python
#coding=utf-8
__author__ = 'Administrator'
'''
数据库连接
'''

import redis
import configs


class DBUtil:
    r = None

    def __init__(self):
        self.r = redis.Redis(host=configs.HOST, port=configs.PORT, db=configs.DB)