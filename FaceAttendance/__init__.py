# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/17 19:31:50
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   flask app 初始化
'''

# here put the import lib

from flask import Flask
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from config import config
from .utils import wechat_api
# from .utils.face_utils import face_utils_cls


# moment = Moment()
db = SQLAlchemy()
# pagedown = PageDown()

# face_tools = face_utils_cls()
wechat = wechat_api()


def create_app(config_name):
    app = Flask(__name__, static_folder='./static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # moment.init_app(app)
    db.init_app(app)

    # @app.before_first_request
    # def init():
    #     print('-- 第一次请求进来再加载face类 --')
    #     global face_tools
    #     global wechat
    #     # face_tools = face_utils_cls()
    #     wechat = wechat_api()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .face import face as face_blueprint
    app.register_blueprint(face_blueprint, url_prefix='/face')

    return app
