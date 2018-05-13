# -*- coding:utf-8 -*-

from aip import AipOcr


APP_ID = 'test'
API_KEY = 'xx'
SECRET_KEY = 'xx'


class OcrUtil(object):

    # 读取图片
    def open_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_image_verfy_code(self, file):
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        result = aipOcr.basicGeneral(self.open_file_content(file))
        try:
            verification_code = result.get('words_result')[0]['words']
            return verification_code
        except Exception, e:
            raise

