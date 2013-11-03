#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
菜单模型
'''


class Menu:
    id = None
    title = None

    def __init__(self, id_, title_):
        self.id = id_
        self.title = title_