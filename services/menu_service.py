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

        dic_menus = self.db_util.get_list_objects('menu', start, end)

        list_menu = []
        for menu in dic_menus:
            menu = Menu(menu)
            list_menu.append(menu)

        return list_menu