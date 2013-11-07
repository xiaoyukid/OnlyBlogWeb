#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
全局设置模型
'''


class Blog:
    name = 'My Blog'
    sub_title = 'this is a blog'
    username = ''
    password = ''

    def __init__(self, name, password, sub_title, username):
        self.name = name
        self.password = password
        self.sub_title = sub_title
        self.username = username