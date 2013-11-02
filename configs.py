#coding=utf-8
__author__ = 'tonghs'

from views.index import *

PAGE_SIZE = 10
HOST = 'localhost'
PORT = 6379
DB = 0

urls = (
    "^/$", index,
    "/get_posts/(.*)", posts
)