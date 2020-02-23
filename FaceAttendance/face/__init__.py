# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/17 22:28:43
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   人脸识别接口
'''

# here put the import lib
from flask import Blueprint, render_template

face = Blueprint('face', __name__)