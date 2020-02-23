# -*- encoding: utf-8 -*-
'''
@File    :   wechat_utils.py
@Time    :   2020/02/17 11:42:52
@Author  :   Ricardo 
@Version :   1.0
@Contact :   GeekRicardozzZ@gmail.com
@Desc    :   None
'''

# here put the import lib

import requests
import json



class wechat_api():
    """
    微信接口实现
    """
    def __init__(self):
        self.appid = "wxdc1bc9b0ff34165e"
        self.secret = "e75ecb4d532d167e92ec24f2f4c1e0bc"

    def code2session(self, code):
        '''
        @description: 用小程序发来的code换取用户登录态
        @param code{str} 小程序暂时登陆态的code
        @return: openid	用户唯一标识
                session_key	string	会话密钥
                unionid	string	用户在开放平台的唯一标识符，在满足 UnionID 下发条件的情况下会返回，详见 UnionID 机制说明。
                errcode	number	错误码
                errmsg	string	错误信息
        '''
        if(code):
            url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(self.appid, self.secret, code)
            try:
                res = requests.get(url)
                if(res.status_code == 200):
                    reobj = json.loads(res.text)
                    print('sessiong_key_res:',reobj)
                    if(not reobj.get('errcode') or reobj.get('errcode') == 0):
                        return reobj
                    else:
                        print(reobj['errmsg'])
                        return reobj
                else:
                    return {'errcode': 12, 'errmsg': "微信服务器无响应，请重试！"}
            except Exception as e:
                print(e)
                return {'errcode': 13, 'errmsg': "网络错误，请重试！"}
        else:
            return {'errcode': 14, 'errmsg': "请重新获取code"} 

    def getAccessToken(self):
        """
        Desc: 获取AccessToken
            
        Args: 
            appip : 
            secret：
        Returns: 
            access_token	string	获取到的凭证
            expires_in		number	凭证有效时间，单位：秒。目前是7200秒之内的值。
            errcode			number	错误码
            errmsg			string	错误信息
        Raises:
            
        """
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(self.appid, self.secret)
        try:
            res = requests.get(url)
            if(res.status_code == requests.codes.ok):
                reobj = json.loads(res.text)
                print('accesstoken_res:', reobj.text)
        except Exception as e:
            return {'errcode': 12, 'errmsg': "微信服务器无响应，请重试！"}
        