from hytest import *
from lib.webapi import SMS
import json,traceback

# 用例模块清除
def test_teardown():
    # 获取所有客户信息
    customer_list = SMS.customer_list1('list_customer',100,1,'').json()["retlist"]
    INFO(json.dumps(customer_list,ensure_ascii=False,indent=4))
    # 删除所有用户信息
    for customer in customer_list:
        INFO(customer)
        customer_del = SMS.customer_del("del_customer",customer["id"]).json()
        INFO(json.dumps(customer_del,ensure_ascii=False,indent=4))

class customerAdd0101:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "客户名、电话号码、地址 均符合接口规范 customerAdd0101"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ：阿乐，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','阿乐','18193458090','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "id": 46,
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected["ret"]==ret["ret"])
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
            STEP(4, '查看添加后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                                    "id": 5041,
                                    "name": "阿乐",
                                    "phonenumber": "18193458090"
                                },
                                {
                                    "address": "上海华山路777号",
                                    "id": 4,
                                    "name": "上海人民医院",
                                    "phonenumber": "14456789017"
                                }
                            ],
                            "total": 2
                        }
            STEP(5, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"] == ret1["name"]
                        and expected1["retlist"][0]["phonenumber"] == ret1["phonenumber"]
                        and expected1["retlist"][0]["address"] == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerAdd0102:
    name = "已有10个客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "添加一个客户，客户名、电话号码、地址 均符合接口规范 customerAdd0102"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            cusyomer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(cusyomer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ：阿乐，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','阿乐','18193458090','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "id": 46,
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected["ret"]==ret["ret"])
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
            STEP(4, '查看添加后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                "ret": 0,
                "retlist": [
                    {
                        "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                        "id": 5041,
                        "name": "阿乐",
                        "phonenumber": "18193458090"
                    },
                    {
                        "address": "上海华山路777号",
                        "id": 4,
                        "name": "上海人民医院",
                        "phonenumber": "14456789017"
                    }
                ],
                "total": 2
            }
            STEP(5, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"] == ret1["name"]
                        and expected1["retlist"][0]["phonenumber"] == ret1["phonenumber"]
                        and expected1["retlist"][0]["address"] == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerAdd0103:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "添加一个客户，客户名字字段缺失 customerAdd0103"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            cusyomer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(cusyomer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ：''，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','','18193458090','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "msg": "req body format error\nKey: 'Body.Data.Name' Error:Field validation for 'Name' failed on the 'required' tag",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected==ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerAdd0104:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "添加一个客户，客户名字字段重复2次 customerAdd0104"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            cusyomer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(cusyomer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ,"阿乐","阿乐"，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','阿乐阿乐','18193458090','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "id": 5221,
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected["ret"] == ret["ret"])
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerAdd0105:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "添加一个客户，电话号码字段缺失 customerAdd0105"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            cusyomer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(cusyomer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ,"阿乐"，参数phonenumber：""，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','阿乐','','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "msg": "req body format error\nKey: 'Body.Data.Phonenumber' Error:Field validation for 'Phonenumber' failed on the 'required' tag",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected==ret)
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())
class customerAdd0106:
    name = "没有客户，没有药品，没有订单（请求头携带登录成功的session id），" \
           "添加一个客户，电话号码字段重复2次 customerAdd0106"
    def setup(self):
        #调用登录接口
        SMS.login('byhy', '88888888')
        #新增10个客户
        for item in range(1,10):
            cusyomer_add = SMS.customer_add('add_customer',f'武汉市桥西医院{item}',
                             '13345679934',f'武汉市桥西医院北路{item}')
            INFO(json.dumps(cusyomer_add.json(),ensure_ascii=False,indent=4))
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(),ensure_ascii=False,indent=4))
            STEP(2, '参数action：add_customer ，参数name ,"阿乐"，参数phonenumber："18193458090"，"18193458090",'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerAdd = SMS.customer_add('add_customer','阿乐','1819345809018193458090','甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerAdd.json()
            INFO(ret)
            expected = {
                            "id": 5221,
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确',expected["ret"] == ret["ret"])
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
        except Exception:
            INFO(traceback.format_exc())





