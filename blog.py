#coding=utf-8
__author__ = 'Administrator'

import web
from utils import configs

urls = configs.urls

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()