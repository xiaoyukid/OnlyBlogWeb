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

    def __init__(self, id_, title_, content_):
        self.id = id_
        self.title = title_
        self.content = content_