#coding=utf-8
__author__ = 'Administrator'
import redis
import configs


class DBUtil:
    r = None

    def __init__(self):
        self.r = redis.Redis(host=configs.HOST, port=configs.PORT, db=configs.DB)
        #self.r = redis.Redis(host='localhost', post=6379, db=0)

    def get_object_ids(self, obj_name, start, end):
        list_ids = self.r.lrange(obj_name + ':ids', start, end)
        return list_ids

    def get_object_by_id(self, obj_name, id):
        obj = self.r.hgetall(obj_name + ":" + id)

        return obj