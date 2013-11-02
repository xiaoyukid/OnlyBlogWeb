#coding=utf-8
__author__ = 'Administrator'
import redis
from configs import *


class DBUtil:
    r = None

    def __init__(self):
        self.r = redis.Redis(host=HOST, post=PORT, db=DB)

    def get_object_ids(self, obj_name, start, end):
        list_ids = self.r.lrange(obj_name + ':ids', start, end)
        return list_ids

    def get_object_by_id(self, obj_name, id):
        obj = self.r.hgetall(obj_name + ":" + id)

        return obj