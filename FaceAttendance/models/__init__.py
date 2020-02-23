# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/17 11:08:33
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   None
'''

# here put the import lib

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:ricardo@localhost/faceattendance"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from .sign_record import SignRecord
from .user import UserRole, User

