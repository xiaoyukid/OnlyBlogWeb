#!/usr/bin/env python
#coding=utf-8
from configs import settings
from services.post_service import PostService
from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
菜单管理服务
'''


class TagService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def add_tag(self, name):
        """
        添加/更新tag
        """
        score = self.db_util.r.zincrby('tags', name)
        self.db_util.r.zadd('tags', name, score)

        return score

    def get_tags(self):
        """
        获取所有标签
        """
        dic_menus = self.db_util.r.zrange('tags', 0, 5)

        list_menu = []
        for menu in dic_menus:
            list_menu.append(menu)

        return list_menu

    def get_post_by_tag(self, name, page):
        """
        获取该标签下所有文章
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_post_ids = self.db_util.r.lrange('tag:' + name, start, end)

        list_post = []
        for id in list_post_ids:
            post = PostService().get_post(id)
            list_post.append(post)

        return list_post

    def add_to_tag(self, name, value):
        self.db_util.r.lpush(name, value)
