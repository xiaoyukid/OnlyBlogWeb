#!/usr/bin/env python
#coding=utf-8
from configs import settings, db
from utils.db_util import DBUtil

__author__ = 'tonghs'
'''
菜单管理服务
'''


class TagService:
    r = None

    def __init__(self):
        self.r = DBUtil().r

    def add_tag(self, name):
        """
        添加/更新tag
        """
        id = self.r.incrby(db.STR_TAG_COUNT)
        self.r.set(db.STR_TAG_ID_TO_NAME % int(id), name)
        self.r.set(db.STR_TAG_NAME_TO_ID % name, id)
        self.r.lpush(db.L_TAG_IDS, id)

        return id

    def get_tag(self, start=0, end=-1):
        """
        获取所有标签
        """
        tags = self.r.zrange('tags', start, end)

        return tags
    
    def get_tag_by_name(self, name):
        """
        根据tag名获取id
        """
        id = self.r.get(db.STR_TAG_NAME_TO_ID % name)
        # 如果标签不存在
        if not id:
            id = self.add_tag(name)

        return id

    def get_post_by_tag(self, name, page):
        """
        获取该标签下所有文章
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_post_ids = self.r.lrange('tag:' + name, start, end)

        list_post = []
        #for id in list_post_ids:
        #    post = PostService().get_post(id)
        #    list_post.append(post)

        return list_post

    def add_to_tag(self, id, post_id):
        self.r.lpush(db.L_TAG_POSTS % int(id), post_id)