#coding=utf-8
__author__ = 'Administrator'


class post:
    title = None
    content = None
    category = None
    tag = None

    def __init__(self, title, content, category, tag):
        self.title = title
        self.content = content
        self.category = category
        self.tag = tag