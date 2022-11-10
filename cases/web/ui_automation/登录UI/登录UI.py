from hytest import *
from selenium.webdriver.common.by import By
from lib.webui import open_browser,user_login

# 用例初始化
def test_setup():
    open_browser()
    user_login()
# 用例清楚
def test_teardown():
    wd = GSTORE['wd']
    wd.quit()

class UILogin001:
    name = "输入正确的用户名和密码，登录成功 UILogin001"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, '输入用户名 byhy')
        wd.find_element(By.ID,'username').send_keys('byhy')
        STEP(2, '输入密码 88888888')
        wd.find_element(By.ID,'password').send_keys('88888888')
        STEP(3, '点击登录按钮')
        wd.find_element(By.TAG_NAME,'button').click()
        STEP(4,'获取左侧菜单信息')
        eles = wd.find_elements(By.CSS_SELECTOR,'.sidebar-menu li span')
        menuText = [ele.text  for ele in eles]
        INFO(menuText)
        expected = ['客户', '药品', '订单', '其它菜单','']
        STEP(5,'断言，左侧菜单检查')
        CHECK_POINT('左侧菜单检查',expected == menuText)
class UILogin002:
    name = "输入正确的用户名,错误密码，登录失败 UILogin002"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, '输入用户名 byhy')
        wd.find_element(By.ID, 'username').send_keys('byhy')
        STEP(2, '输入密码 888888880')
        wd.find_element(By.ID, 'password').send_keys('888888880')
        STEP(3, '点击登录按钮')
        wd.find_element(By.TAG_NAME, 'button').click()
        alert_content = wd.switch_to.alert.text
        INFO(alert_content)
        expected = '登录失败 : 用户名或者密码错误'
        STEP(5, '断言，检查菜单栏')
        CHECK_POINT('弹窗提示检查', expected == alert_content)
class UILogin003:
    name = "输入正确的用户名，密码为空，登录失败 UILogin003"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, '输入用户名 byhy')
        wd.find_element(By.ID, 'username').send_keys('byhy')
        STEP(2, '输入密码为空')
        wd.find_element(By.ID, 'password').send_keys('')
        STEP(3, '点击登录按钮')
        wd.find_element(By.TAG_NAME, 'button').click()
        alert_content=wd.switch_to.alert.text
        INFO(alert_content)
        expected = '请输入密码'
        STEP(5, '断言，检查菜单栏')
        CHECK_POINT('弹窗提示检查', expected == alert_content)
class UILogin004:
    name = "输入错误的用户名和密码，登录失败 UILogin004"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, '输入用户名 byhyo')
        wd.find_element(By.ID, 'username').send_keys('byhyo')
        STEP(2, '输入密码 888888880')
        wd.find_element(By.ID, 'password').send_keys('888888880')
        STEP(3, '点击登录按钮')
        wd.find_element(By.TAG_NAME, 'button').click()
        alert_content=wd.switch_to.alert.text
        INFO(alert_content)
        expected = '登录失败 : 用户名或者密码错误'
        STEP(5, '断言，检查菜单栏')
        CHECK_POINT('弹窗提示检查', expected == alert_content)
class UILogin005:
    name = "输入用户名和密码为空，登录失败 UILogin005"
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, '输入用户名为空')
        wd.find_element(By.ID, 'username').send_keys('')
        STEP(2, '输入密码为空')
        wd.find_element(By.ID, 'password').send_keys('')
        STEP(3, '点击登录按钮')
        wd.find_element(By.TAG_NAME, 'button').click()
        alert_content=wd.switch_to.alert.text
        INFO(alert_content)
        expected = '请输入用户名'
        STEP(5, '断言，检查菜单栏')
        CHECK_POINT('弹窗提示检查', expected == alert_content)
