# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/20 21:33:11
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   sign init
'''

# here put the import lib
from flask import render_template, Blueprint

sign = Blueprint('sign', __name__)

from . import views, errors