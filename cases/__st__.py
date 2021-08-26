from hytest import *
from lib.get_time import *


def suite_setup():
    """
    用于整个套件的初始化操作
    """
    data = time_stamp
    # GSTORE是一个用来存储全局变量的dict
    GSTORE['data'] = data
    # INFO中的内容只会出现在生成的报表中，不会打印在终端
    INFO(f'这是首次初始化,获得初始数据data:{data}')


def suite_teardown():
    """
    用于整个套件的清除操作
    """
    INFO(f'这是最后一次清除')
