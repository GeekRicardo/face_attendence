# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/02/18 18:44:55
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   utils.__init__
'''

# here put the import lib
import random
import time
import hashlib

from .wechat_utils import wechat_api
from .face_utils import face_utils_cls


def encrty_string(oldstr, _random_str=""):
    """
    Desc: 将字符串加密
    
        原字符串和时间戳和随机字符串混淆md5加密而得
        
    Args: 
        :param oldstr 需要加密的字符串 
    Returns: 
        
    Raises:
        
    """
    if(_random_str == "" or not len(_random_str) == 16 ):
        strs = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./;'[]\`-=<>?:"{}|+_)(*&^%$#@!~"`"""
        _random_str = ''.join(random.sample(strs, 16))
    _time_stamp = str(round(time.time() * 1000))
    al = _time_stamp + oldstr + _random_str
    m = hashlib.md5()
    m.update(al)
    return m.hexdigest()
    
