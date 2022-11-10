from hytest import *
from lib.webapi import SMS
import json,traceback

#用例模块清除
def test_teardown():
    #获取所有客户信息
    customer_list = SMS.customer_list1('list_customer',100,1,'').json()["retlist"]
    INFO(json.dumps(customer_list,ensure_ascii=False,indent=4))
    # 删除所有用户信息
    for customer in customer_list:
        INFO(customer)
        customer_del = SMS.customer_del("del_customer",customer["id"]).json()
        INFO(json.dumps(customer_del,ensure_ascii=False,indent=4))

class customerList0001:
    name = "没有客户，没有药品，没有订单（请求头没有携带登录成功的session id），pagenum=1，" \
           "pagesize=10，keywords=空字符串） customerList0001"
    def teststeps(self):
        try:
            STEP(1,'参数action：list_customer，参数：pagesize：100，参数pagenum：1，参数keywords：空字符串')
            allCustomer = SMS.customer_list('list_customer',100,1,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 302,
                            "msg":  "未登录",
                            "redirect": "/mgr/sign.html"
                        }
            STEP(2, '断言，返回的消息体数据正确')
            CHECK_POINT('返回消息体正确',expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0002:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=1，" \
           "pagesize=10，keywords=空字符串） customerList0002"
    def teststeps(self):
        try:
            STEP(1,'调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2,'参数action：list_customer，参数：pagesize：1，参数pagenum：10，'
                   '参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',1,10,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [],
                            "total": 1
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected == ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0003:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=hello，" \
           "pagesize=10，keywords=空字符串） customerList0003"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：hello，参数pagenum：10，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer', 'hello', 10, '')
            ret = allCustomer.json()
            expected = {
                            "msg": "bad pagesize:hello",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0004:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=1，" \
           "pagesize=hello，keywords=空字符串） customerList0004"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：1，参数pagenum：hello，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer', 1,'hello', '')
            ret = allCustomer.json()
            expected = {
                            "msg": "bad pagenum:hello",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0005:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum缺失，" \
           "pagesize=10，keywords=空字符串） customerList0005"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：缺失，参数pagenum：10，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer','',10, '')
            ret = allCustomer.json()
            expected = {
                            "msg": "bad pagesize:",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0006:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=1，" \
           "pagesize缺失，keywords=空字符串） customerList0006"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：1，参数pagenum：缺失，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',1,'', '')
            ret = allCustomer.json()
            expected = {
                            "msg": "bad pagenum:",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0007:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=1，" \
           "pagesize=10，keywords缺失） customerList0007"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：1，参数pagenum：10，参数keywords：缺失')
            allCustomer = SMS.customer_list1('list_customer',1,10,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [],
                            "total": 1
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0008:
    name = "已有10个客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=1，" \
           "pagesize=10，keywords空字符串） customerList0008"
    def setup(self):
        #调用登录接口
        login = SMS.login('byhy', '88888888')
        INFO(json.dumps(login.json(),ensure_ascii=False,indent=4))
        #新增10个客户
        for item in range(1,10):
            customer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(customer_add.json(),ensure_ascii=False,indent=4))

    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：1，参数pagenum：10，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',1,10,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "上海华山路777号",
                                    "id": 4,
                                    "name": "上海人民医院",
                                    "phonenumber": "14456789017"
                                }
                            ],
                            "total": 10
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0009:
    name = "已有10个客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=2，" \
           "pagesize=10，keywords空字符串） customerList0009"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            customer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(customer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：2，参数pagenum：10，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',2,10,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [],
                            "total": 10
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0010:
    name = "已有10个客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=3，" \
           "pagesize=10，keywords空字符串） customerList0010"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            customer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(customer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：3，参数pagenum：10，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',3,10,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [],
                            "total": 10
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerList0011:
    name = "已有10个客户，没有药品，没有订单（请求头携带登录成功的session id，pagenum=3，" \
           "pagesize=5，keywords空字符串） customerList0011"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            customer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(customer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：list_customer，参数：pagesize：3，参数pagenum：5，参数keywords：空字符串')
            allCustomer = SMS.customer_list1('list_customer',3,5,'')
            ret = allCustomer.json()
            expected = {
                            "ret": 0,
                            "retlist": [],
                            "total": 10
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
        except Exception:
            INFO(traceback.format_exc())