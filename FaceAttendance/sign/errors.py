# -*- encoding: utf-8 -*-
'''
@File    :   error.py
@Time    :   2020/02/17 22:49:12
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   错误处理
'''

# here put the import lib
from flask import render_template
from . import sign

@sign.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@sign.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500