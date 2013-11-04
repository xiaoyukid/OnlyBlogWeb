#!/usr/bin/env python
#coding=utf-8
import configs
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

    def get_menus(self):
        """
        获取所有菜单
        """
        dic_menus = self.db_util.get_list_objects('categorys', 0, 5)

        list_menu = []
        for menu in dic_menus:
            list_menu.append(menu)

        return list_menu

    def get_post_by_category(self, name, page):
        """
        获取分类下所有文章
        """
        start = (int(page) - 1) * int(configs.PAGE_SIZE)
        end = int(page) * int(configs.PAGE_SIZE)

        list_post_ids = self.db_util.get_list_objects('category:' + name, start, end)

        list_post = []
        for id in list_post_ids:
            post = PostService().get_post(id)
            list_post.append(post)

        return list_post