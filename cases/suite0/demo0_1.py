from hytest import *


def suite_setup():
    INFO('这是demo0_1的初始化')


def suite_teardown():
    INFO('这是demo0_1的清除')


class case_2(object):
    name = '演示2'
    tags = ['冒烟测试', '接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示2的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示2的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data'] + 1
        INFO(f'这是演示2测试步骤中的data:{data}')
        CHECK_POINT('这是演示2中的断言', data == GSTORE['data'])


class case_3(object):
    name = '演示3'
    tags = ['接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示3的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示3的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data']
        INFO(f'这是演示3测试步骤中的data:{data}')
        CHECK_POINT('这是演示3中的断言', data == data / 0)
