from hytest import *


force_tags = ['demo0_0测试']


def suite_setup():
    INFO('这是demo0_0的初始化')


def suite_teardown():
    INFO('这是demo0_0的清除')


class case_0(object):
    name = '演示0'
    tags = ['冒烟测试', '接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        GSTORE['data'] = GSTORE['data'] * 10
        INFO(f'这是演示0的初始化,data:{GSTORE["data"]}')

    def teardown(self):
        # 用于单个用例的初始化操作
        GSTORE['data'] = GSTORE['data'] / 10
        INFO(f'这是演示0的清除操作,data:{GSTORE["data"]}')

    def teststeps(self):
        STEP(1, '这是第一步')
        GSTORE["data"] = GSTORE['data'] + 1
        INFO(f'这是演示0测试步骤中的data:{GSTORE["data"]}')
        STEP(2, '这是第二步')
        CHECK_POINT('这是演示0中的断言', GSTORE["data"] == GSTORE["data"])


class case_1(object):
    name = '演示1'
    tags = ['接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示1的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示1的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data']
        INFO(f'这是演示1测试步骤中的data:{data}')
        CHECK_POINT('这是演示1中的断言', data == data)
