# -*- coding:utf-8 -*-
import time

from de_except import VerificationError

from splinter import Browser

from baidu_ocr_util import  OcrUtil
from jd_verfy import JdVerfy
import contant


class SecKill(object):
    def __init__(self):
        self.JdVerfy = JdVerfy()
        self.ocr = OcrUtil()

    def login(self, name, passwd):
        browser = Browser(driver_name="chrome")
        url = 'https://www.jd.com/'
        browser.visit(url)
        browser.click_link_by_text("你好，请登录")
        #坑一
        browser.click_link_by_text("账户登录")
        browser.fill("loginname", name)  # 填写账户密码
        browser.fill("nloginpwd", passwd)
        try:
            self.JdVerfy.get_jd_verfy_code()
            content = self.ocr.get_image_verfy_code(contant.img_path)
            print 'jd verfy code is %s', content
        except Exception:
            raise VerificationError('验证码获取异常')
        browser.fill('authcode', content)
        time.sleep(3)
        browser.find_by_id("loginsubmit").click()





seckill = SecKill()
seckill.login('xx','xx')
