from hytest import *


def suite_setup():
    INFO('这是demo1_1的初始化')


def suite_teardown():
    INFO('这是demo1_1的清除')


class case_6(object):
    name = '演示6'
    tags = ['冒烟测试', '接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data'] * 10
        INFO(f'这是演示6的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data'] / 10
        INFO(f'这是演示6的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data'] + 1
        INFO(f'这是演示6测试步骤中的data:{data}')
        CHECK_POINT('这是演示6中的断言', data == data)


class case_7(object):
    name = '演示7'
    tags = ['冒烟测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data'] / 0
        INFO(f'这是演示7的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data'] / 10
        INFO(f'这是演示7的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data'] + 1
        INFO(f'这是演示7测试步骤中的data:{data}')
        CHECK_POINT('这是演示7中的断言', data == data)
