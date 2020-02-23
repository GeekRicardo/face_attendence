# -*- encoding: utf-8 -*-
'''
@File    :   view.py
@Time    :   2020/02/20 21:34:53
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   sign view
'''

# here put the import lib
from flask import render_template, redirect, request, jsonify

import os, datetime

from . import sign
from .. import db,  wechat
from ..models.sign_record import SignRecord
from ..models.user import UserRole, User

@sign.route('/signin', methods=['GET','POST'])
def signin():
    """
    Desc: 签到，根据不同时间判断不同时间段的签到
        
    Args: 
        GET : 判断是否签到
        POST：进行签到流程，图片识别等流程
    Returns: 
        
    Raises:
        
    """
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass