from hytest import *
from lib.webapi import SMS
import json

# #用例套件初始化
# def suite_setup():
#     #获取登录信息
#     SMS.login('byhy', '88888888')
#     INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
#     # 获取所有客户信息
#     customer_list = SMS.customer_list1('list_customer', 100, 1, '').json()["retlist"]
#     INFO(json.dumps(customer_list, ensure_ascii=False, indent=4))
#     # 删除所有用户信息
#     for customer in customer_list:
#         INFO(customer)
#         customer_del = SMS.customer_del("del_customer", customer["id"]).json()
#         INFO(json.dumps(customer_del, ensure_ascii=False, indent=4))
#
# #用例套件清除
# def suite_teardown():#获取登录信息
#     SMS.login('byhy', '88888888')
#     INFO(json.dumps(SMS.login('byhy', '88888888').json(), ensure_ascii=False, indent=4))
#     # 获取所有客户信息
#     customer_list = SMS.customer_list1('list_customer', 100, 1, '').json()["retlist"]
#     INFO(json.dumps(customer_list, ensure_ascii=False, indent=4))
#     # 删除所有用户信息
#     for customer in customer_list:
#         INFO(customer)
#         customer_del = SMS.customer_del("del_customer", customer["id"]).json()
#         INFO(json.dumps(customer_del, ensure_ascii=False, indent=4))