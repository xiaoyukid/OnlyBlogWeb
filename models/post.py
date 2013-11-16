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
    category = None
    tags = None
    pub_date = None

    def __init__(self, id=None, title=None, content='', category=None, tags=[],
                 pub_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        self.id = id
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
        self.pub_date = pub_date