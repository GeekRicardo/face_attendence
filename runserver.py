# -*- encoding: utf-8 -*-
'''
@File    :   runserver.py
@Time    :   2020/02/18 18:28:20
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   运行服务
'''

# here put the import lib

import os 

from FaceAttendance import create_app, db
from FaceAttendance.models import SignRecord, UserRole, User

from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

# 异步
# from gevent import monkey
# monkey.patch_all()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserRole=UserRole, SignRecord=SignRecord)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=21243, use_debugger=True))
manager.add_command('run', Server(host='0.0.0.0', port=21243, use_debugger=True, ssl_crt='./wechat.crt', ssl_key='./wechat.key'))

if __name__ == '__main__':
    manager.run()
