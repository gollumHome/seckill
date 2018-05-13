# -*- coding:utf-8 -*-

import re
import random
import requests
from lxml import etree


import contant


class JdVerfy(object):

    def __init__(self):
        self.img_path = contant.img_path

    def get_jd_acid_uid(self):
        r = requests.get('https://passport.jd.com/new/login.aspx')
        print r.encoding
        #print r.text
        #print r.cookies
        html = etree.HTML(r.text)
        result = html.xpath('//img[@src2]')
        try:
            for item in result:
                image_path = etree.tostring(item)
            #print image_path
            pattern = r'acid.*" '
            result = re.findall(pattern, image_path)
            temp = result[0].replace('"', '')
            result = temp.split(';')
            #print result
            acid = result[0].split('&')[0]
            uid = result[1].strip()
        except Exception,e:
            print 'get   image_path error'
        return acid, uid

    def get_jd_verfy_code_url(self):
        acid, uid = self.get_jd_acid_uid()
        print acid
        print uid
        yys = '&yys='+self.get_random_str(13)
        #print yys
        url = "https://authcode.jd.com/verify/image?a=1&"+acid+"&"+uid+yys
        return url

    def get_cookie(self):
        f=open(r'cookie.txt','r')#打开所保存的cookies内容文件
        cookies={}#初始化cookies字典变量
        for line in f.read().split(';'):   #按照字符：进行划分读取
            #其设置为1就会把字符串拆分成2份
            name,value=line.strip().split('=',1)
            cookies[name]=value  #为字典cookies添加内容
        return cookies

    def set_requests(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content - Type': 'charset=gbk',
            'Referer': 'https://passport.jd.com/new/login*'
        }
        cookies = self.get_cookie()
        result = requests.get(url, headers=headers, cookies=cookies, verify=False)
        print result.encoding
        return result

    def get_random_str(self, length):
        i = 0
        num_str = ''
        while i < length:
            num_str += str(random.randint(0, 9))
            i = i + 1
        return num_str

    def save_verfy_image(self, img):
        with open(self.img_path, 'wb') as f:
            f.write(img)

    def get_jd_verfy_code(self):
        url = self.get_jd_verfy_code_url()
        print url
        verfy_image = self.set_requests(url)
        print verfy_image
        self.save_verfy_image(verfy_image.content)




