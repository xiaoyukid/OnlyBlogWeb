* 全局设置：
    * 散列:key: blog field:name title password
    * name:博客名 title:博客标题 password:管理密码

* 文章：
    * 文章对象。散列:key: post:文章id field:title:标题 content:内容 pub_date:发布时间 category:分类ID
    * 文章标签。集合:key: post:文章ID:tag member:标签ID
* 文章数/ID：
    * 字符:key: post:counts value:自增ID数
    * incr 获取自增ID
* 文章ID列表：
    * 列表：key:post:ids
    * 存放文章id

* 分类
    * 分类对象。字符:key: category_id_to_name:分类ID value:分类名
    * 字符:key: category_name_to_id:分类名 value:分类ID
    * 分类中的文章。列表:key: category:分类ID:posts member:文章ID
* 分类数/ID
    * 字符: key:category:count
    * incr 获取自增 ID
* 分类列表：
    * 有序集合: key:category:ids member:分类ID score:文章数

* 标签
    * 标签对象。字符:key: tag_id_to_name:标签ID value:分类名
    * 字符:key: tag_name_to_id:标签名 value:ID
    * 该标签文章列表。列表:key: tag:标签ID:posts member:文章ID
* 标签数/ID
    * 字符: key:tag:count
    * incr 获取自增 ID
* 标签列表：
    * 列表:key: tag:ids value:标签ID