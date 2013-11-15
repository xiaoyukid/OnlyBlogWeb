#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
全局设置模型
'''


class Blog:
    name = None
    title = None
    password = None

    def __init__(self, name='My Blog', title='this is a blog', password='tonghs'):
        self.name = name
        self.title = title
        self.password = password