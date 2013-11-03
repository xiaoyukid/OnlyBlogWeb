#!/usr/bin/env python
#coding=utf-8
import configs
from models.menu import Menu
from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
菜单管理服务
'''


class MenuService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def get_menus(self, page):
        """
        获取所有菜单
        """
        start = (int(page) - 1) * int(configs.PAGE_SIZE)
        end = int(page) * int(configs.PAGE_SIZE) - 1

        list_ids = self.db_util.get_object_ids('menu', start, end)

        list_menu = []
        for menu_id in list_ids:
            menu = self.db_util.get_str_obj_by_id('menu', menu_id)
            menu = Menu(menu_id, menu)
            list_menu.append(menu)

        return list_menu