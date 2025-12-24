# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    yonghuxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='手机' )
    shenfenzhenghao=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='身份证号' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True,unique=True,comment='邮箱' )

class loucengzhiyin(Base_model):
    __doc__ = u'''loucengzhiyin'''
    __tablename__ = 'loucengzhiyin'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    louceng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='楼层' )
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    loucengzhiyin=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='楼层指引' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    gengxinshijian=db.Column( db.Date,  nullable=True, unique=False,comment='更新时间' )

class renyuanxinxi(Base_model):
    __doc__ = u'''renyuanxinxi'''
    __tablename__ = 'renyuanxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    gangwei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='岗位' )
    zhaopian=db.Column( db.Text,  nullable=True, unique=False,comment='照片' )
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    gengxinriqi=db.Column( db.Date,  nullable=True, unique=False,comment='更新日期' )

class chayidanganzhiyin(Base_model):
    __doc__ = u'''chayidanganzhiyin'''
    __tablename__ = 'chayidanganzhiyin'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    chadangliucheng=db.Column( db.Text,  nullable=True, unique=False,comment='查档流程' )
    zhuyishixiang=db.Column( db.Text,  nullable=True, unique=False,comment='注意事项' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    gengxinriqi=db.Column( db.Date,  nullable=True, unique=False,comment='更新日期' )

class yijiaojinguanyuyue(Base_model):
    __doc__ = u'''yijiaojinguanyuyue'''
    __tablename__ = 'yijiaojinguanyuyue'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    yuyueshijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='预约时间' )
    danganshuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='档案数量' )
    gongsimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司名称' )
    gongsifenqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司分区' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    shenfenzhenghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证号' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class canguanchadangyuyue(Base_model):
    __doc__ = u'''canguanchadangyuyue'''
    __tablename__ = 'canguanchadangyuyue'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    yuyueshijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='预约时间' )
    yuyueleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='预约类型' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    shenfenzhenghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证号' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class yijiaoyuyuequxiao(Base_model):
    __doc__ = u'''yijiaoyuyuequxiao'''
    __tablename__ = 'yijiaoyuyuequxiao'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    yuyueshijian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='预约时间' )
    danganshuliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='档案数量' )
    gongsimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司名称' )
    gongsifenqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='公司分区' )
    quxiaoyuanyin=db.Column( db.Text,  nullable=True, unique=False,comment='取消原因' )
    quxiaoshijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='取消时间' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    shenfenzhenghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证号' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class canguanchadangyuyuequxiao(Base_model):
    __doc__ = u'''canguanchadangyuyuequxiao'''
    __tablename__ = 'canguanchadangyuyuequxiao'



    __authTables__={'yonghuzhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    diqu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='地区' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    yuyueshijian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='预约时间' )
    yuyueleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='预约类型' )
    quxiaoyuanyin=db.Column( db.Text,  nullable=True, unique=False,comment='取消原因' )
    quxiaoshijian=db.Column( db.DateTime,  nullable=True, unique=False,comment='取消时间' )
    yonghuzhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户账号' )
    yonghuxingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户姓名' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    shenfenzhenghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证号' )
    sfsh=db.Column( db.VARCHAR(255),default='待审核', nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )

class chat(Base_model):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    adminid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='管理员id' )
    ask=db.Column( db.Text,  nullable=True, unique=False,comment='提问' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复' )
    isreply=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='是否回复' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class discussnews(Base_model):
    __doc__ = u'''discussnews'''
    __tablename__ = 'discussnews'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

