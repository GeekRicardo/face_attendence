# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2020/02/17 13:13:48
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   用户类
'''

# here put the import lib


from .. import db
from datetime import datetime

from enum import Enum

class UserRole(Enum):
    """
    desc: 用户角色枚举
        
    Attributes: 
        root{0}: 超级管理员
        admin{1}: 管理员
        leader{2}: 负责人
        staff{3}: 职员
        
    """
    root = 1
    admin = 2
    leader = 3
    staff = 4

class User(db.Model):
    """
    desc: 
        用户基础信息类，包括openid
    Attributes: 
        id {}: 工号
        openid: 小程序openid
        face: 用户人脸关键点信息
        role: 角色
    """
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="工号")
    openid = db.Column(db.String(100), primary_key=True, comment="小程序openid")
    username = db.Column(db.String(50), nullable=False)
    passwd = db.Column(db.String(50), nullable=False)
    face = db.Column(db.String(200), nullable=False, comment="人脸位置信息")
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
    is_del = db.Column(db.Boolean, default=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.staff, nullable=False, comment="用户角色")

    def __init__(self, **kwargs):
        super().__init__()
        if(not len(kwargs) == 0):
            self.id = kwargs.get('id')
            self.openid = kwargs.get('openid')
            self.username = kwargs.get('username')
            self.passwd = kwargs.get('passwd')
            self.phone = kwargs.get('phone')
            self.email = kwargs.get('email')
            self.address = kwargs.get('address')
            self.role = kwargs.get('role') or UserRole.staff
            self.is_del = kwargs.get('is_del') or False
            
    def keys(self):
        return ('id', 'openid', 'username', 'passwd', 'face', 'phone', 'email', 'address', 'create_time', 'is_del', 'role')
    
    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return '\n【 user => %s 】\n' % self.username