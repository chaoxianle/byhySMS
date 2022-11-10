from hytest import *
from lib.webapi import SMS
import json
import traceback

class APILogin001:
    name = "输入正确的用户名和密码，登录成功 APILogin001"
    def teststeps(self):
        try:
            STEP(1,'输入用户名 byhy，输入密码 88888888')
            loginSuccesssfully = SMS.login('byhy','88888888')
            ret = loginSuccesssfully.json()
            expected = {
                            "ret": 0
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class APILogin002:
    name = "输入正确的用户名,错误密码，登录失败 APILogin002"
    def teststeps(self):
        try:
            STEP(1,'输入用户名 byhy，输入密码 888888880')
            loginSuccesssfully = SMS.login('byhy','888888880')
            ret = loginSuccesssfully.json()
            expected = {
                            "msg": "用户名或者密码错误",
                            "ret": 1
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',
                        expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class APILogin003:
    name = "输入正确的用户名，密码为空，登录失败 APILogin003"
    def teststeps(self):
        try:
            STEP(1,'输入用户名 byhy，输入密码为空')
            loginSuccesssfully = SMS.login('byhy','')
            ret = loginSuccesssfully.json()
            expected = {
                            "msg": "用户名或者密码错误",
                            "ret": 1
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',
                        expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class APILogin004:
    name = "输入错误的用户名和密码，登录失败 APILogin004"
    def teststeps(self):
        try:
            STEP(1,'输入用户名 byhyo，输入密码 888888880')
            loginSuccesssfully = SMS.login('byhyo','888888880')
            ret = loginSuccesssfully.json()
            expected = {
                            "msg": "用户名或者密码错误",
                            "ret": 1
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',
                        expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class APILogin005:
    name = "输入用户名和密码为空，登录失败 APILogin005"
    def teststeps(self):
        try:
            STEP(1,'输入用户名为空，输入密码为空')
            loginSuccesssfully = SMS.login('','')
            ret = loginSuccesssfully.json()
            expected = {
                            "msg": "用户名或者密码错误",
                            "ret": 1
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',
                        expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())