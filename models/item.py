#coding=utf-8
__author__ = 'Administrator'

from utils.db_util import DBUtil

class Item:
    def __init__(self):
        pass

    def get_item(self):
        conn = DBUtil.get_conn()