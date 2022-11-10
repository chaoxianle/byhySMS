from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By

def open_browser():
    INFO('打开浏览器')
    # 加上参数，禁止 chromedriver 日志写屏
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)  # 这里指定 options 参数
    wd.implicitly_wait(5)
    GSTORE['wd'] = wd

def user_login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.maximize_window()

def mgr_login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.maximize_window()
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.ID, 'password').send_keys('88888888')
    wd.find_element(By.TAG_NAME, 'button').click()
