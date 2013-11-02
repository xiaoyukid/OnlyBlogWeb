#coding=utf-8
__author__ = 'tonghs'
from utils.db_util import DBUtil
import configs

class PostService:
    db_util = None

    def __init__(self):
        self.db_util = DBUtil()

    def get_posts(self, page):
        start = (int(page) - 1) * int(configs.PAGE_SIZE)
        end = int(page) * int(configs.PAGE_SIZE) - 1

        list_ids = self.db_util.get_object_ids('posts', start, end)

        list_post = []
        for post_id in list_ids:
            post = self.db_util.get_object_by_id('post', post_id)
            list_post.append(post)

        return list_post