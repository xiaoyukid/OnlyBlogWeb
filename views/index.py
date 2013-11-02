#coding=utf-8
__author__ = 'Administrator'
import web

import utils
from services.post_service import PostService


render = web.template.render("templates/")


class index:
    def __init__(self):
        pass

    def GET(self):
        return render.index()


class posts:
    post_service = None

    def __init__(self):
        self.post_service = PostService()

    def GET(self, page):
        list_post = self.post_service.get_posts(page)

        return list_post