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

    def get_list_objects(self, obj_name, start, end):
        """
        获取对象列表
        """
        list_ids = self.r.lrange(obj_name, start, end)
        return list_ids

    def get_hash_obj(self, name):
        """
        获取散列对象
        """
        obj = self.r.hgetall(name)

        return obj

    def get_hash_attr(self, hash_name, attr_name):
        """
        获取散列对象的属性
        """
        obj = self.r.hget(hash_name, attr_name)

        return obj

    def get_str_obj(self, obj_name):
        """
        获取字符串对象
        """
        obj = self.r.get(obj_name)

        return obj

    def get_incr_count(self, name):
        return self.r.incr(name)

    def add_hash_obj(self, name, obj):
        self.r.hmset(name, obj)

    def add_to_list_obj(self, name, value):
        self.r.lpush(name, value)