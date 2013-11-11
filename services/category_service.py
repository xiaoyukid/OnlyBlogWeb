#!/usr/bin/env python
#coding=utf-8
from configs import settings
from services.post_service import PostService
from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
菜单管理服务
'''


class CategoryService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def add_category(self, name):
        """
        增加/更新分类
        """
        score = self.db_util.r.zincrby('categories', name)
        self.db_util.r.zadd('categories', name, score)

        return score

    def add_to_category(self, name, value):
        """
        向分类列表添加文章
        """
        self.db_util.r.lpush(name, value)

    def get_menus(self):
        """
        获取所有菜单
        """
        dic_menus = self.db_util.r.zrange('categories', 0, 5)

        list_menu = []
        for menu in dic_menus:
            list_menu.append(menu)

        return list_menu

    def get_post_by_category(self, name, page):
        """
        获取分类下所有文章
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_post_ids = self.db_util.r.lrange('category:' + name, start, end)

        list_post = []
        for id in list_post_ids:
            post = PostService().get_post(id)
            list_post.append(post)

        return list_post