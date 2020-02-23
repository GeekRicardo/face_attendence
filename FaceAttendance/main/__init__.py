# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/17 19:01:41
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   flask 视图包
'''

# here put the import lib
from flask import render_template, Blueprint

main = Blueprint('main', __name__)

from . import views, errors
