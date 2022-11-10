from hytest import *
from lib.webapi import SMS
from lib.webapi_public import customer_modify_setup
import json,traceback

#用例模块清除
def test_teardown():
    # 获取所有客户信息
    customer_list = SMS.customer_list1('list_customer', 100, 1, '').json()["retlist"]
    INFO(json.dumps(customer_list, ensure_ascii=False, indent=4))
    # 删除所有用户信息
    for customer in customer_list:
        INFO(customer)
        customer_del = SMS.customer_del("del_customer", customer["id"]).json()
        INFO(json.dumps(customer_del, ensure_ascii=False, indent=4))
class customerModify0201:
    name = "没有客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "修改客户ID为一个不存在的ID customerModify0201"
    def teststeps(self):
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO('登录返回结果')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：1，参数name ：阿乐，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',1,'阿乐','18193458090',
                                                 '甘肃省庆阳市西峰区朔州西路庆化苑二区')
            INFO('修改后客户信息')
            ret = customerModify.json()
            expected = {
                            "msg": "customer id not exist",
                            "ret": 2
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
        except Exception:
            INFO(traceback.format_exc())
class customerModify0202:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "只修改客户名称，修改客户ID为一个存在的ID customerModify0202"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ："阿乐"，参数phonenumber："13345679934"，'
                    '参数address ：武汉市桥西医院北路')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'阿乐','13345679934',
                                                 '武汉市桥西医院北路')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1,ensure_ascii=False,indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "武汉市桥西医院北路",
                                    "id": 4994,
                                    "name": "阿乐",
                                    "phonenumber": "13345679934"
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"] == ret1["name"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0203:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，只修改客户电话 customerModify0203"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：武汉市桥西医院，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'武汉市桥西医院','18193458090',
                                                 '武汉市桥西医院北路')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret,ensure_ascii=False,indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1,ensure_ascii=False,indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "武汉市桥西医院北路",
                                    "id": 5003,
                                    "name": "武汉市桥西医院",
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["phonenumber"] == ret1["phonenumber"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0204:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，只修改客户地址 customerModify0204"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：武汉市桥西医院，参数phonenumber："13345679934"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'武汉市桥西医院','13345679934',
                                                 '甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                                    "id": 5008,
                                    "name": "武汉市桥西医院",
                                    "phonenumber": "14456789017"
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["address"]
                        == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0205:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，修改客户名称和客户电话 customerModify0205"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：阿乐，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'阿乐','18193458090',
                                                 '武汉市桥西医院北路')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "武汉市桥西医院北路",
                                    "id": 5010,
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"]
                        == ret1["name"] and expected1["retlist"][0]["phonenumber"]
                        == ret1["phonenumber"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0206:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，修改客户名称和地址 customerModify0206"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：阿乐，参数phonenumber："13345679934"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'阿乐','13345679934',
                                                 '甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                                    "id": 5012,
                                    "name": "阿乐",
                                    "phonenumber": "13345679934"
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"]
                        == ret1["name"] and expected1["retlist"][0]["address"]
                        == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0207:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，修改客户电话和地址 customerModify0207"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：武汉市桥西医院，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'武汉市桥西医院','18193458090',
                                                 '甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                                    "id": 5015,
                                    "name": "武汉市桥西医院",
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["phonenumber"]
                        == ret1["phonenumber"] and expected1["retlist"][0]["address"]
                        == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0208:
    name = "已经存在一个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，修改客户名称，客户电话和地址 customerModify0208"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：阿乐，参数phonenumber："18193458090"，'
                    '参数address ：甘肃省庆阳市西峰区朔州西路庆化苑二区')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'阿乐','18193458090',
                                                 '甘肃省庆阳市西峰区朔州西路庆化苑二区')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "甘肃省庆阳市西峰区朔州西路庆化苑二区",
                                    "id": 5016,
                                    "name": "阿乐",
                                    "phonenumber": "18193458090"
                                },
                                {
                                    "address": "武汉市桥西医院北路",
                                    "id": 5015,
                                    "name": "武汉市桥西医院",
                                    "phonenumber": "13345679934"
                                },
                                {
                                    "address": "上海华山路777号",
                                    "id": 4,
                                    "name": "上海人民医院",
                                    "phonenumber": "14456789017"
                                }
                            ],
                            "total": 3
                        }
            STEP(5, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"]
                        == ret1["name"] and expected1["retlist"][0]["phonenumber"]
                        == ret1["phonenumber"] and expected1["retlist"][0]["address"]
                        == ret1["address"])
        except Exception:
            INFO(traceback.format_exc())
class customerModify0209:
    name = "已经存在两个客户，没有药品，没有订单，（请求头携带登录成功的session id），" \
           "客户ID为一个存在的ID，修改客户名称和已经存在的客户相同 customerModify0209"
    def setup(self):
        customer_modify_setup()
    def teststeps(self):
        customer_add = GSTORE["customer_add"]
        try:
            STEP(1, '调用用户登录接口')
            SMS.login('byhy', '88888888')
            INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
            STEP(2, '参数action：modify_customer，参数id：customer_add，参数name ：f"{customer_list_name}"，参数phonenumber："18193458090"，'
                    '参数address ：f"{customer_list_address}"')
            customerModify = SMS.customer_modify('modify_customer',customer_add,'武汉市桥西医院','13345679934',
                                                 '武汉市桥西医院北路')
            ret = customerModify.json()
            INFO('修改后客户信息')
            INFO(json.dumps(ret, ensure_ascii=False, indent=4))
            expected = {
                            "ret": 0
                        }
            STEP(3, '断言，返回的消息体数据正确')
            CHECK_POINT('返回的消息体数据正确', expected == ret)
            STEP(4, '查看修改后客户信息')
            customer_list_address = SMS.customer_list1('list_customer', 100, 1, '')
            ret1 = customer_list_address.json()["retlist"][0]
            INFO(json.dumps(ret1, ensure_ascii=False, indent=4))
            expected1 = {
                            "ret": 0,
                            "retlist": [
                                {
                                    "address": "武汉市桥西医院北路",
                                    "id": 5020,
                                    "name": "武汉市桥西医院",
                                    "phonenumber": "13345679934"
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
            CHECK_POINT('返回的消息体数据正确', expected1["retlist"][0]["name"]
                        == ret1["name"])
        except Exception:
            INFO(traceback.format_exc())