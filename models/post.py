#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonghs'
'''
文章模型
'''


class Post:
    id = None
    title = None
    content = None
    category = None

    def __init__(self, id_, title_, content_, category_):
        self.id = id_
        self.title = title_
        self.content = content_
        self.category = category_