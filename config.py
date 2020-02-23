# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2020/02/17 18:42:45
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   flask settings
'''

# here put the import lib
import os
import datetime

# 获取项目根目录
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Desc: flask 配置基类
        
    Attributes: 
        {}: 
    """
    SECRET_KEY  = os.environ.get('SECRET_KEY') or 'df6e9244-5175-11ea-ae8e-52540011c219'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=3)
    HOST = '0.0.0.0'
    PORT = 5000
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    """
    Desc: 开发环境配置
        
    Attributes: 
        {}: 
    """
    
    DEBUG = False
    PROCESSES = 2
    THREADED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "mysql://root:ricardo@localhost/faceattendance"


class TestingConfig(Config):
    """
    Desc: 测试环境配置
        
    Attributes: 
        {}: 
    """
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        "mysql://root:ricardo@localhost/faceattendance"
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """
    Desc: 线上版本配置
        
    Attributes: 
        {}: 
    """
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "mysql://root:ricardo@localhost/faceattendance"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


class DockerConfig(ProductionConfig):
    """
    Desc: Docker环境配置
        
    Attributes: 
        {}: 
    """
    
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.INFO)
        app.logger.addHandler(syslog_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}

