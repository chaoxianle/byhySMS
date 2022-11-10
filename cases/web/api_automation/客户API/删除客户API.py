from hytest import *
from lib.webapi import SMS
from lib.webapi_public import customer_modify_setup
import json,traceback

class customerDel0301:
    name = "没有客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "删除客户ID为一个不存在的ID customerDel0301"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：del_customer，参数id：1')
            customerDel = SMS.customer_del('del_customer',1)
            ret = customerDel.json()
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
        except Exception:
            INFO(traceback.format_exc())
class customerDel0302:
    global customer_add
    name = "没有客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "删除客户ID为一个不存在的ID customerDel0302"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：del_customer，参数id：1')
            customerDel = SMS.customer_del('del_customer',customer_add)
            ret = customerDel.json()
            INFO(ret)
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
        except Exception:
            INFO(traceback.format_exc())