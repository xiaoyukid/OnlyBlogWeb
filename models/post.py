#coding=utf-8
import datetime

__author__ = 'Administrator'


class Post:
    """
    文章module
    """
    id = None
    title = None
    content = None
    pub_date = None

    def __init__(self, id, title, content, pub_date=datetime.datetime.now()):
        self.id = id
        self.title = title
        self.content = content
        self.pub_date = pub_date