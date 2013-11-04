* 全局设置：
 * 散列：blog name sub_title
 * 如：blog name Blog sub_title this is a blog

* 文章：
 * 散列：post:文章id title content category tag
 * 如：post:1 title test content test category linux tag linux
 * 文章数：str：post:counts
 * 文章ID列表：列表：post:ids

* 分类
 * 列表：category:分类名 文章id
 * 如：category:linux 1

* 分类列表：
 * 列表：categorys 分类名
 * 如：categorys linux
 * ps：菜单列表取分类的前五个，根据可根据文章数目作为权重排列

