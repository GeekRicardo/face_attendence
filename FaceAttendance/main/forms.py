# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2020/02/19 19:15:41
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   表单类
'''

# here put the import lib
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
# from flask_pagedown.fields import PageDownField
from ..models import Role, User

class UserRegisterForm(FlaskForm):
    username = StringField('姓名', validators=[Length(0, 64), DataRequired(message='用户名不能为空')])
                                                            # ,render_kw={
                                                            #     'placeholder':"用输入用户名",
                                                            #     "class":"form-control"
                                                            # })
    passwd = PasswordField('密码', validators=[Length(0, 64), 
                                            DataRequired(message='密码不能为空')])
    reppwd = PasswordField('确认密码', validators=[Length(0, 64), 
                                            DataRequired(message='请再次输入密码'),
                                            EqualTo('passwd',message="两次密码不一致")])
    phone = StringField('联系方式', validators=[Length(0, 12), 
                                            DataRequired(message='请输入联系方式'),
                                            Regexp('1\d{10}',message="手机号码格式不正确")])
    email = StringField('邮箱', validators=[Length(0, 64), 
                                            DataRequired(message='请输入常用邮箱'),
                                            Email(message='邮箱格式不正确!')])
    address = StringField('现住址', validators=[Length(0, 64), 
                                            DataRequired(message='请输入您的住址')])
    submit = SubmitField('注册')