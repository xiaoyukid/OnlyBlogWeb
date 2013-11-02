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

    def get_object_ids(self, obj_name, start, end):
        '''
        获取对象ID列表
        '''
        list_ids = self.r.lrange(obj_name + ':ids', start, end)
        return list_ids

    def get_object_by_id(self, obj_name, id):
        '''
        根据ID获取对象
        '''
        obj = self.r.hgetall(obj_name + ":" + id)

        return obj