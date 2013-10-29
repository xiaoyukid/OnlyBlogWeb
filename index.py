#coding=utf-8
__author__ = 'Administrator'

import web
from views.index import Index


urls = (
    "/.*", Index
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()