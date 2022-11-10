from hytest import *
from lib.webui import open_browser,mgr_login

#套件初始化
def suite_setup():
    open_browser()
    mgr_login()

#套件清除
def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()
