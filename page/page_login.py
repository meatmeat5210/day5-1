

from base.base import Base
import page

# 新建 登录页面对象类
class PageLogin(Base):

    # 输入用户名 封装
    def page_input_username(self,username):
        self.base_input(page.login_username, username)

    # 输入密码 封装
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录 封装
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 组装登录方法 给业务层调用
    def page_login(self,username,pwd):
        self.page_input_username(username )
        self.page_input_pwd(pwd)
        self.page_click_login()