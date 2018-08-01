# coding:utf-8

from mongoengine import Document,DateTimeField,IntField,StringField,URLField
from datetime import datetime

# 定义mongodb数据库数据模型
class Article(Document):
    '''
    文章信息
    '''
    title = StringField()   # 文章标题
    content_url = StringField()   # 文章链接
    content = StringField()   # 文章内容
    source_url = StringField()   # 原文链接
    digest = StringField()   # 文章摘要
    cover = URLField(validation=None)   # 封面图
    push_time = DateTimeField()   #推送时间

    read_num = IntField(default=0)   # 阅读数
    like_num = IntField(default=0)   # 点赞数
    comment_num = IntField(default=0)   # 评论数
    reward_num = IntField(default=0)   # 赞赏数
    author = StringField()   # 作者

    publish_date = DateTimeField(default=datetime.now)   # 数据生成时间
    update_date = DateTimeField(default=datetime.now)   # 最后更新时间