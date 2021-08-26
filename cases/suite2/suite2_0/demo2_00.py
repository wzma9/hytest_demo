from hytest import *


def suite_setup():
    INFO('这是demo2_00的初始化')


def suite_teardown():
    INFO('这是demo2_00的清除')


class case_9(object):
    name = '演示9'
    tags = ['冒烟测试', '接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data2 = GSTORE['data2']
        INFO(f'这是演示9的初始化,data:{data2}')

    def teardown(self):
        # 用于单个用例的初始化操作
        INFO(f'这是演示9的清除操作')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data'] + GSTORE['data2']
        INFO(f'这是演示9测试步骤中的data:{data}')
        CHECK_POINT('这是演示9中的断言', data == GSTORE["data"] + GSTORE["data2"])


class case_10(object):
    name = '演示10'
    tags = ['接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data2']
        INFO(f'这是演示10的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data2']
        INFO(f'这是演示10的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data2']
        INFO(f'这是演示10测试步骤中的data:{data}')
        CHECK_POINT('这是演示10中的断言', data == data)
