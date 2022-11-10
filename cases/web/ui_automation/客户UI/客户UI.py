from hytest import *
from selenium.webdriver.common.by import By
import time

class UIMgr_001:
    name = "添加客户后并删除  UIMgr_001"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1,'点击左侧客户菜单')
        wd.find_element(By.XPATH,'//*[@id="root"]/aside/section/ul/li[2]/a').click()
        STEP(2,'点击添加客户按钮')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/button').click()
        STEP(3,'输入客户名 阿乐')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[1]/input').send_keys('阿乐')
        STEP(4,'输入联系电话 18193458090')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[2]/input').send_keys('18193458090')
        STEP(5,'输入地址 甘肃省庆阳市西峰区庆化苑二区6号楼1单元1002室')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[1]/div[3]/textarea').send_keys('甘肃省庆阳市西峰区庆化苑二区6号楼1单元1002室')
        STEP(6,'点击创建按钮')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        STEP(7, '检查添加信息')
        # 找到 列表最上面的一栏
        item = wd.find_elements(By.CLASS_NAME,'search-result-item')[0]
        fields = item.find_elements(By.TAG_NAME,'span')[:6]
        texts = [field.text for field in fields]
        INFO(texts)
        # 预期内容为
        expected = [
            '客户名：',
            '阿乐',
            '联系电话：',
            '18193458090',
            '地址：',
            '甘肃省庆阳市西峰区庆化苑二区6号楼1单元1002室'
        ]

        CHECK_POINT('客户信息和添加内容一致 ',
                    texts == expected)
        STEP(8,'点击删除按钮')
        wd.find_element(By.XPATH,'//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        time.sleep(1)
        alert = wd.switch_to.alert
        alert.accept()
