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

# 文章标签关联
S_POST_TAGS = 'post:%d:tags'

# 分类对象
STR_CATEGORY_ID_TO_NAME = 'category_id_to_name:%d'
STR_CATEGORY_NAME_TO_ID = 'category_name_to_id:%s'
# 分类列表
Z_CATEGORY_IDS = 'category:ids'
# 分类计数
STR_CATEGORY_COUNT = 'category:count'
# 该分类文章列表
L_CATEGORY_POSTS = 'category:%d:posts'

# 标签对象
STR_TAG_ID_TO_NAME = 'tag_id_to_name:%d'
STR_TAG_NAME_TO_ID = 'tag_name_to_id:%s'
# 标题列表
L_TAG_IDS = 'tag:ids'
# 标签计数
STR_TAG_COUNT = 'tag:count'
# 该标签下的文章列表
L_TAG_POSTS = 'tag:%d:posts'



