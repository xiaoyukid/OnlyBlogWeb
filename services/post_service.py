#!/usr/bin/env python
#coding=utf-8
from configs import db
from configs import settings
from models.post import Post
from services.tag_service import TagService
from services.category_service import CategoryService

__author__ = 'tonghs'
'''
文章服务
用于文章的管理
'''


class PostService:
    r = None

    def __init__(self):
        self.r = db.r

    def get_posts(self, page):
        """
        获取所有文章

        @param page 当前页
        """
        start = (int(page) - 1) * int(settings.PAGE_SIZE)
        end = int(page) * int(settings.PAGE_SIZE) - 1

        list_ids = self.r.lrange(db.L_POST_IDS, start, end)

        list_post = []
        for post_id in list_ids:
            dic_post = self.r.hgetall(db.H_POST % post_id)
            post = Post(id=post_id, title=dic_post[db.H_POST_TITLE], content=dic_post[db.H_POST_CONTENT])
            list_post.append(post)

        return list_post

    def get_post(self, post_id):
        """
        根据ID获取post
        """
        dic_post = self.r.hgetall(db.H_POST % int(post_id))
        post = Post(id=post_id, title=dic_post[db.H_POST_TITLE], content=dic_post[db.H_POST_CONTENT])

        return post

    def add_post(self, post):
        """
        添加文章
        """

        # 获取ID
        id = self.r.incr(db.STR_POST_COUNT)
        post.id = id

        # 设置文章标签
        self.set_tags(post)

        # 设置分类
        self.set_category(post)

        #文章ID列表
        self.r.lpush(db.L_POST_IDS, id)

        dic_post = post.__dict__
        del dic_post['tags']
        #增加文章
        self.r.hmset(db.H_POST % int(id), dic_post)

        return id

    def set_tags(self, post):
        # 添加/更新tag
        tag_ids = []
        for tag in post.tags:
            tag_id = TagService().get_tag_by_name(tag)
            TagService().add_to_tag(tag_id, post.id)
            tag_ids.append(tag_id)

        self.r.sadd(db.S_POST_TAGS % int(post.id), tag_ids)


    def set_category(self, post):
        # 获取分类ID（当分类不存在时添加）
        category = CategoryService().get_category_by_name(post.category)
        post.category = category
        # 添加文章到分类文章集合
        CategoryService().add_to_category(category, post.id)

    def update_post(self, post):
        """
        添加文章
        """

        #增加文章
        self.r.hset(db.H_POST % int(post.id), 'title', post.title)
        self.r.hset(db.H_POST % int(post.id), 'content', post.content)

        return post.id