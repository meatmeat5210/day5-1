import os
import sys
sys.path.append(os.getcwd())

from base.get_driver import get_driver
from page.page_login import PageLogin

class TestLogin:
    #setup
    #获取driver
    def setup(self):
        # 获取driver
        self.driver = get_driver()
        #获取page页面对象
        self.login = PageLogin(self.driver)

    #teardown
    #关闭浏览器
    def teardown(self):
        self.driver.quit()

    #测试方法
    def text_login(self, username="111", pwd="123456"):
        self.login.page_login(username, pwd)