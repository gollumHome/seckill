#! usr/bin/python
#coding=utf-8


class VerificationError(Exception):
    def __init__(self, ErrorInfo):
        super(VerificationError,self).__init__() #初始化父类
        self.errorinfo=ErrorInfo

    def __str__(self):
        return self.errorinfo
