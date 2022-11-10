from hytest import *
from pprint import pprint
import requests,config

# 服务器地址
testUrl = GSTORE['testUrl']

class SMSAPI:
    # 控制台打印
    def _printResponse(self, response):
        print('\n\n---------- HTTP response * brgin ----------')
        print(response.status_code)
        for k, v in response.headers.items():
            print(f'{k}：{v}')
        print('')
        print(response.content.decode('utf8'))
        print('---------- HTTP response * end ----------\n\n')

    #登录API
    def login(self,username,password):
        # 创建 Session 对象
        self.s = requests.Session()
        response = self.s.post(url=testUrl+'/api/mgr/signin',
                                 data=
                                 {
                                    "username":username, #用户名
                                    "password":password  #密码
                                 })
        self._printResponse(response)
        return response

    # 列出所有客户接口（不携带session）
    def customer_list(self, action, pagesize, pagenum, keywords):
        response = requests.get(url=testUrl + '/api/mgr/customers',
                              params={
                                  "action": action,  # 必填项，填写值为 list_customer
                                  "pagesize": pagesize,  # 必填项，分页的 每页获取多少条记录
                                  "pagenum": pagenum,  # 必填项，获取第几页的信息
                                  "keywords": keywords  # 可选项， 里面包含的多个过滤关键字，关键字之间用 空格 分开
                              })
        self._printResponse(response)
        return response

    #列出所有客户接口（携带session）
    def customer_list1(self,action,pagesize,pagenum,keywords):
        response = self.s.get(url=testUrl+'/api/mgr/customers',
                                params={
                                    "action"  :action,   #必填项，填写值为 list_customer
                                    "pagesize":pagesize, #必填项，分页的 每页获取多少条记录
                                    "pagenum" :pagenum,  #必填项，获取第几页的信息
                                    "keywords":keywords  #可选项， 里面包含的多个过滤关键字，关键字之间用 空格 分开
                                })
        self._printResponse(response)
        return response

    #新增客户接口（携带session）
    def customer_add(self,action,name,phonenumber,address):
        response = self.s.post(url=testUrl+'/api/mgr/customers',
                               headers={'Content-Type': 'application/json'},
                               json={
                                        "action":action,                # action 字段固定填写 add_customer 表示添加一个客户
                                        "data":{
                                            "name":name,                # name 字段长度范围是 2-20
                                            "phonenumber":phonenumber,  # phonenumber 字段长度范围是 8-15
                                            "address":address           # address 字段长度范围是 2-100
                                        }
                                    })
        self._printResponse(response)
        return response

    #修改客户信息接口
    def customer_modify(self,action,id,name,phonenumber,address):
        response = self.s.put(url=testUrl+'/api/mgr/customers',
                              headers={'Conten-Type':'application/json'},
                              json={
                                        "action":action,                 # action 字段固定填写 modify_customer 表示修改一个客户的信息
                                        "id": id,                        # id 字段为要修改的客户的id号
                                        "newdata":{
                                            "name":name,                # name 客户名
                                            "phonenumber":phonenumber,  # phonenumber 联系电话
                                            "address":address           # address 地址
                                        }
                                    })
        self._printResponse(response)
        return response

    #删除客户信息接口
    def customer_del(self,action,id):
        response = self.s.post(url=testUrl+'/api/mgr/customers',
                               headers={'Content-Type':'application/json'},
                               json={
                                        "action":action,  # action 字段固定填写 del_customer 表示删除一个客户
                                        "id": id          # id 字段为要删除的客户的id号
                                    })
        self._printResponse(response)
        return response

SMS = SMSAPI()