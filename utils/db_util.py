#coding=utf-8
__author__ = 'Administrator'
import pymongo


class DBUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_object(obj_name):
        conn = pymongo.Connection('localhost', 27017)
        db = conn.test
        obj = db.post
        objs = obj.find()

        return objs
