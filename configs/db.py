#coding=utf-8
import redis
from configs import settings
__author__ = 'Administrator'

# redis
r = redis.Redis(host=settings.HOST, port=settings.PORT, db=settings.DB)

# 全局设置
H_BLOG = 'blog'
BLOG_NAME = 'name'
BLOG_TITLE = 'title'
BLOG_PASSWORD = 'password'

# 文章相关
# 文章
H_POST = 'post:%d'
H_POST_TITLE = 'title'
H_POST_CONTENT = 'content'
H_POST_PUB_DATE = 'pub_date'

# 自增文章ID
STR_POST_COUNT = 'post:count'
# 文章ID列表
L_POST_IDS = 'post:ids'