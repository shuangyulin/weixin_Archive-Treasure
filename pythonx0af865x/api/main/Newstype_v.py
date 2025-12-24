# coding:utf-8
__author__ = "ila"

import logging, os, json, configparser
import time
import numbers
import requests
from werkzeug.utils import redirect

from flask import request, jsonify,session
from sqlalchemy.sql import func,and_,or_,case
from sqlalchemy import cast, Integer,Float
from api.models.brush_model import *
from . import main_bp
from utils.codes import *
from utils.jwt_auth import Auth
from configs import configs
from utils.helper import *
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from utils.baidubce_api import BaiDuBce
from api.models.config_model import config



# 注册接口
@main_bp.route("/pythonx0af865x/newstype/register", methods=['POST'])
def pythonx0af865x_newstype_register():
    if request.method == 'POST':
        msg = {'code': normal_code, 'message': 'success', 'data': [{}]}
        req_dict = session.get("req_dict")


        error = newstype.createbyreq(newstype, newstype, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = "注册用户已存在"
        else:
            msg['data'] = error

        return jsonify(msg)

# 登录接口
@main_bp.route("/pythonx0af865x/newstype/login", methods=['GET','POST'])
def pythonx0af865x_newstype_login():
    if request.method == 'GET' or request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        req_model = session.get("req_dict")
        try:
            del req_model['role']
        except:
            pass


        datas = newstype.getbyparams(newstype, newstype, req_model)
        if not datas:
            msg['code'] = password_error_code
            msg['msg']='密码错误或用户不存在'
            return jsonify(msg)


        req_dict['id'] = datas[0].get('id')
        try:
            del req_dict['mima']
        except:
            pass


        return Auth.authenticate(Auth, newstype, req_dict)


# 登出接口
@main_bp.route("/pythonx0af865x/newstype/logout", methods=['POST'])
def pythonx0af865x_newstype_logout():
    if request.method == 'POST':
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

# 重置密码接口
@main_bp.route("/pythonx0af865x/newstype/resetPass", methods=['POST'])
def pythonx0af865x_newstype_resetpass():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success"}

        req_dict = session.get("req_dict")

        if req_dict.get('mima') != None:
            req_dict['mima'] = '123456'

        error = newstype.updatebyparams(newstype, newstype, req_dict)

        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['msg'] = '密码已重置为：123456'
        return jsonify(msg)

# 获取会话信息接口
@main_bp.route("/pythonx0af865x/newstype/session", methods=['GET'])
def pythonx0af865x_newstype_session():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "data": {}}
        req_dict={"id":session.get('params').get("id")}
        msg['data']  = newstype.getbyparams(newstype, newstype, req_dict)[0]

        return jsonify(msg)

# 分类接口（后端）
@main_bp.route("/pythonx0af865x/newstype/page", methods=['GET'])
def pythonx0af865x_newstype_page():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        userinfo = session.get("params")

        try:
            __hasMessage__=newstype.__hasMessage__
        except:
            __hasMessage__=None
        if __hasMessage__ and __hasMessage__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None and newstype!='chat':
                req_dict["userid"]=session.get("params").get("id")

        tablename=session.get("tablename")
        if tablename=="users" :
            try:
                pass
            except:
                pass
        else:
            mapping_str_to_object = {}
            for model in Base_model._decl_class_registry.values():
                if hasattr(model, '__tablename__'):
                    mapping_str_to_object[model.__tablename__] = model

            try:
                __isAdmin__=mapping_str_to_object[tablename].__isAdmin__
            except:
                __isAdmin__=None
            try:
                __authSeparate__ =mapping_str_to_object[tablename].__authSeparate__
            except:
                __authSeparate__ = None

            if __isAdmin__!="是" and __authSeparate__ == "是" and session.get("params")!=None:
                req_dict["userid"]=session.get("params").get("id")
            else:
                try:
                    del req_dict["userid"]
                except:
                    pass

            # 当前表也是有管理员权限的表
            if  __isAdmin__ == "是" and 'newstype' != 'forum':
                if req_dict.get("userid") and 'newstype' != 'chat':
                    del req_dict["userid"]
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if tablename!="users" and 'newstype'[:7]!='discuss'and "userid" in newstype.getallcolumn(newstype,newstype):
                    req_dict["userid"] = session.get("params").get("id")

        clause_args = []
        or_clauses = or_(*clause_args)

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = newstype.page(newstype, newstype, req_dict, or_clauses)
        return jsonify(msg)

# 排序接口
@main_bp.route("/pythonx0af865x/newstype/autoSort", methods=['GET'])
def pythonx0af865x_newstype_autosort():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        req_dict['sort']='clicktime'
        req_dict['order']='desc'

        try:
            __browseClick__= newstype.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ =='是':
            req_dict['sort']='clicknum'
        elif __browseClick__ =='时长':
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = newstype.page(newstype, newstype, req_dict)

        return jsonify(msg)

#查询单条数据
@main_bp.route("/pythonx0af865x/newstype/query", methods=['GET'])
def pythonx0af865x_newstype_query():
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{}}
        req_dict = session.get("req_dict")
        query = db.session.query(newstype)
        for key, value in req_dict.items():
            query = query.filter(getattr(newstype, key) == value)
        query_result = query.first()
        query_result.__dict__.pop('_sa_instance_state', None)
        msg['data'] = query_result.__dict__
        return jsonify(msg)

# 分页接口（前端）
@main_bp.route("/pythonx0af865x/newstype/list", methods=['GET'])
def pythonx0af865x_newstype_list():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success",  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']
            
        userinfo = session.get("params")

        try:
            __foreEndListAuth__=newstype.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users" and session.get("params")!=None:
                req_dict['userid']=session.get("params").get("id")

        tablename=session.get("tablename")

        if 'luntan' in 'newstype':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]


        if 'discuss' in 'newstype':
            if 'userid' in req_dict.keys():
                del req_dict["userid"]

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = newstype.page(newstype, newstype, req_dict)
        return jsonify(msg)

# 保存接口（后端）
@main_bp.route("/pythonx0af865x/newstype/save", methods=['POST'])
def pythonx0af865x_newstype_save():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        for key in req_dict:
            if req_dict[key] == '':
                req_dict[key] = None

        error= newstype.createbyreq(newstype, newstype, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)

# 添加接口（前端）
@main_bp.route("/pythonx0af865x/newstype/add", methods=['POST'])
def pythonx0af865x_newstype_add():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        try:
            __foreEndListAuth__=newstype.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=session.get("tablename")
            if tablename!="users":
                req_dict['userid']=session.get("params").get("id")

        error= newstype.createbyreq(newstype, newstype, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
            return jsonify(msg)
        else:
            msg['data'] = error
        return jsonify(msg)

# 踩、赞接口
@main_bp.route("/pythonx0af865x/newstype/thumbsup/<id_>", methods=['GET'])
def pythonx0af865x_newstype_thumbsup(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=newstype.getbyid(newstype, newstype,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = newstype.updatebyparams(newstype, newstype, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 获取详情信息（后端）
@main_bp.route("/pythonx0af865x/newstype/info/<id_>", methods=['GET'])
def pythonx0af865x_newstype_info(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data = newstype.getbyid(newstype, newstype, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #浏览点击次数
        try:
            __browseClick__= newstype.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__  and  "clicknum"  in newstype.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}
            ret=newstype.updatebyparams(newstype,newstype,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 获取详情信息（前端）
@main_bp.route("/pythonx0af865x/newstype/detail/<id_>", methods=['GET'])
def pythonx0af865x_newstype_detail(id_):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data = newstype.getbyid(newstype, newstype, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #浏览点击次数
        try:
            __browseClick__= newstype.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__ and "clicknum" in newstype.__table__.columns:
            click_dict={"id":int(id_),"clicknum":str(int(data[0].get("clicknum") or 0)+1)}
            ret=newstype.updatebyparams(newstype,newstype,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return jsonify(msg)

# 更新接口
@main_bp.route("/pythonx0af865x/newstype/update", methods=['POST'])
def pythonx0af865x_newstype_update():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")
        if req_dict.get("mima") and "mima" not in newstype.__table__.columns :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in newstype.__table__.columns :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = newstype.updatebyparams(newstype, newstype, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error


        return jsonify(msg)

# 删除接口
@main_bp.route("/pythonx0af865x/newstype/delete", methods=['POST'])
def pythonx0af865x_newstype_delete():
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = session.get("req_dict")

        error=newstype.delete(
            newstype,
            req_dict
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return jsonify(msg)

# 投票接口
@main_bp.route("/pythonx0af865x/newstype/vote/<int:id_>", methods=['POST'])
def pythonx0af865x_newstype_vote(id_):
    '''
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success"}


        data= newstype.getbyid(newstype, newstype, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=newstype.updatebyparams(newstype,newstype,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return jsonify(msg)














#分类列表
@main_bp.route("/pythonx0af865x/newstype/lists", methods=['GET'])
def pythonx0af865x_newstype_lists():
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": []}
        list,_,_,_,_ = newstype.page(newstype,newstype,{})
        msg['data'] = list
        return jsonify(msg)


