# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/02/17 11:43:20
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   None
'''

# here put the import lib


from flask import render_template, redirect, request, jsonify, send_from_directory

import os, time
import cv2
import numpy as np
from os import environ
# import tensorflow as tf

from . import main
from .. import db,  wechat
from ..models.sign_record import SignRecord
from ..models.user import UserRole, User

# from settings import *



@main.route('/')
def index():
    return "main/index..."

@main.route('/favicon.ico')
def getresources():
    print(request.path)
    return send_from_directory('static', request.path[1:])

@main.route('/login', methods=['GET', 'POST'])
def login():
    """
    desc: 用于用户身份验证
    使用code换取sessionid和openid
    param code:{str}
    return:
        :errcode
            :10 未获得code
            :11 未注册用户信息
            :12 微信服务器无响应
            :13 网络错误，暂时无法请求微信服务器
            :14 未正确接收code
            :-1 系统繁忙，此时请开发者稍候再试
            :40029 code 无效
            :45011 频率限制，每个用户每分钟100次
            :0 请求成功
    """ 
    code = request.args.get('code')
    if code:
        sess_dict = wechat.code2session(code)
        if not sess_dict.get('errmsg'):
            print('openid:' + sess_dict['openid'], '\nsession_key' + sess_dict['session_key'])
            user = db.session.query(User).filter_by(openid=sess_dict['openid']).first()
            if user:
                print(user, sess_dict)
                return jsonify(sess_dict)
            else:
                print("未注册")
                return jsonify({'errcode': 11, 'errmsg': '未注册用户信息'})
        else:
            return jsonify(sess_dict)
    else:
        return jsonify({'errcode': 10, 'errmsg': '未获得code'})


@main.route('/getuserinfo/<openid>')
def get_user_info(openid):
    """
    Desc: 登录session_key 有效期间获取用户信息
        
    Args: 
        :openid openid 
    Returns: 
        
    Raises:
        
    """
    # openid = request.args.get('openid')
    openid = openid.strip()
    user = db.session.query(User).filter_by(openid=openid).first()
    if user:
        return jsonify({
            'errcode': 0,
            'errmsg': "",
            'user': user
            })
    else:
        return jsonify({
            'errcode': 1,
            'errmsg': "无此用户绑定或openid错误",
        })