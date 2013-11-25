#!/usr/bin/env python
#coding=utf-8
from configs import settings
from utils.db_util import DBUtil
from configs import db

__author__ = 'tonghs'
'''
菜单管理服务
'''


class CategoryService:
    r = None

    def __init__(self):
        self.r = DBUtil().r

    def add_category(self, name):
        """
        增加/更新分类
        """
        id = self.r.incrby(db.STR_CATEGORY_COUNT)
        self.r.set(db.STR_CATEGORY_ID_TO_NAME % int(id), name)
        self.r.set(db.STR_CATEGORY_NAME_TO_ID % name, id)
        self.r.zadd(db.Z_CATEGORY_IDS, id, 0)

        return id

    def add_to_category(self, id, post_id):
        """
        向分类列表添加文章
        """
        self.r.lpush(db.L_CATEGORY_POSTS % int(id), post_id)
        #增加该分类的文章数
        self.r.zincrby(db.Z_CATEGORY_IDS, id)

    def get_category(self, start=0, end=-1):
        """
        获取分类列表
        @param start:
        @param end:
        """
        categories = []
        ids = self.r.zrange(db.Z_CATEGORY_IDS, start, end)
        for id in ids:
            category = self.get_category_by_id(id)
            categories.append(category)

        return categories

    def get_category_by_id(self, id):
        """
        根据分类ID获取分类名
        """
        name = self.r.get(db.STR_CATEGORY_ID_TO_NAME % int(id))

        return name

    def get_category_by_name(self, name):
        """
        根据分类名获取ID
        """
        id = self.r.get(db.STR_CATEGORY_NAME_TO_ID % name)

        return id


    def get_menus(self):
        """
        获取所有菜单
        """
        menus = self.get_category(0, 5)

        return menus

    def get_post_ids_by_category(self, id, page):
        """
        获取分类下所有文章
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_post_ids = self.r.lrange(db.L_CATEGORY_POSTS % int(id), start, end)

        return list_post_ids