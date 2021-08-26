from hytest import *


force_tags = ['suite0测试']


def suite_setup():
    data = GSTORE['data'] + 1
    INFO(f'这是suite0中的初始化,data：{data}')


def suite_teardown():
    data = GSTORE['data'] - 1
    INFO(f'这是suite0中清除,data：{data}')
