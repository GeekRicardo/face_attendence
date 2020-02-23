# -*- encoding: utf-8 -*-
'''
@File    :   sign_record.py
@Time    :   2020/02/17 11:09:12
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   None
'''

# here put the import lib

from .. import db
from datetime import datetime

class SignRecord(db.Model):
    """
    desc: 签到记录
        
    Attributes: 
        is_late {Boolean}: 是否迟到
    """
    
    __tablename__ = "sign_record"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    sign_time = db.Column(db.DateTime, default=datetime.now())
    is_late = db.Column(db.Boolean, default=False)
    late_time = db.Column(db.Integer, default=0, comment="迟到时长（分钟），默认0")
    
    def __init__(self, **kwargs):
        super.__init__()
        if(not len(kwargs) == 0):
            self.id = kwargs.get('id')
            self.userid = kwargs.get('userid')
            self.sign_time = kwargs.get('sign_time') or datetime.now()
            self.late_time = kwargs.get('late_time') or 0
            self.is_late = kwargs.get('is_late') or False
            
    def __str__(self):
        return '<s%> -> [s%] s%' % (self.id, self.userid, self.is_late if self.is_late else '')