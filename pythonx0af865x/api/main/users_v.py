# coding:utf-8
__author__ = "ila"

from flask import session, jsonify, request

from . import main_bp
from utils.codes import *
from api.models.user_model import users
from utils.jwt_auth import Auth
from utils import message as mes


@main_bp.route("/pythonx0af865x/users/login", methods=['GET',"POST"])
def pythonx0af865x_users_login():
    if request.method == 'GET' or request.method == 'POST':
        msg = {'code': normal_code, 'msg': 'success'}
        req_dict = session.get("req_dict")

        datas = users.getbyparams(users, users, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = '登录失败'
            return jsonify(msg)

        req_dict['id'] = datas[0].get('id')
        return Auth.authenticate(Auth, users, req_dict)


@main_bp.route("/pythonx0af865x/users/register", methods=['POST'])
def pythonx0af865x_users_register():
    if request.method == 'POST':
        msg = {'code': normal_code, 'msg': 'success'}
        req_dict = session.get("req_dict")

        error = users.createbyreq(users, users, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)

@main_bp.route("/pythonx0af865x/users/session", methods=['GET'])
def pythonx0af865x_users_session():
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "data": {}}

        req_dict={"id":session.get('params').get("id")}
        msg['data']  = users.getbyparams(users, users, req_dict)[0]
        return jsonify(msg)

@main_bp.route("/pythonx0af865x/users/logout", methods=['POST'])
def pythonx0af865x_users_logout():
    if request.method == 'POST':
        msg = {
            "msg": "退出成功",
            "code": 0
        }
        req_dict = session.get("req_dict")

        return jsonify(msg)

@main_bp.route("/pythonx0af865x/users/page", methods=['GET'])
def pythonx0af865x_users_page():
    '''
    获取
    :return:
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}, "pagination": {}}
        req_dict = session.get('req_dict')
        msg['data']['list'], msg['pagination']['page'], msg['pagination']['pages'], msg['pagination']['total'], \
        msg['pagination']['limit'] = users.page(users, users, req_dict)
        return jsonify(msg)


@main_bp.route("/pythonx0af865x/users/info/<id>", methods=['GET'])
def pythonx0af865x_users_info(id):
    '''
    '''
    if request.method == 'GET':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        data= users.getbyid(users, users, int(id))
        if len(data)>0:
            msg['data'] =data[0]
        return jsonify(msg)


@main_bp.route("/pythonx0af865x/users/save", methods=['POST'])
def pythonx0af865x_users_save():
    '''
    创建订单信息
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code}

        req_dict = session.get('req_dict')

        if users.count(users, users, {"username":req_dict["username"]})>0:
            msg['code'] = crud_error_code
            msg['msg'] = "账号已存在"
            return jsonify(msg)

        error = users.createbyreq(users, users, req_dict)
        if error!=None and error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return jsonify(msg)


@main_bp.route("/pythonx0af865x/users/update", methods=['POST'])
def pythonx0af865x_users_update():
    '''
    更新订单信息
    在此更新支付状态
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        req_dict = session.get('req_dict')

        if req_dict.get("mima") and req_dict.get("password"):
            if "mima" not  in users.__table__.columns :
                del req_dict["mima"]
            if  "password" not  in users.__table__.columns :
                del req_dict["password"]

        error = users.updatebyparams(users, users, req_dict)
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = mes.crud_error_code
        return jsonify(msg)


@main_bp.route("/pythonx0af865x/users/delete", methods=['POST'])
def pythonx0af865x_users_delete():
    '''
    删除订单信息
    :return:
    '''
    if request.method == 'POST':
        msg = {"code": normal_code, "msg": "success", "data": {}}

        req_dict = session.get('req_dict')
        error = users.delete(
            users,
            req_dict
        )
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = mes.crud_error_code
        return jsonify(msg)
