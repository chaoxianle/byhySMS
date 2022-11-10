from hytest import *
from lib.webapi import SMS
import json

#封装修改客户信息初始化方法
def customer_modify_setup():
    # 调用登录接口
    SMS.login('byhy', '88888888')
    INFO('登录返回结果')
    INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
    INFO('新增客户id')
    # 新增1个客户
    customer_add = SMS.customer_add('add_customer', '武汉市桥西医院',
                                          '13345679934', '武汉市桥西医院北路').json()["id"]
    INFO(json.dumps(customer_add, ensure_ascii=False, indent=4))
    INFO('新增客户信息')
    customer_list = SMS.customer_list1('list_customer', 100, 1, '').json()["retlist"][0]
    INFO(json.dumps(customer_list, ensure_ascii=False, indent=4))
    GSTORE["customer_add"] = customer_add