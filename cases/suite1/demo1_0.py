from hytest import *


def suite_setup():
    INFO('用例文件初始化失败演示')
    data = GSTORE['data']
    data = data / 0


def suite_teardown():
    INFO('这是demo1_0的清除')


class case_4(object):
    name = '演示4'
    tags = ['冒烟测试', '接口测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示4的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示4的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data']
        INFO(f'这是演示4测试步骤中的data:{data}')
        CHECK_POINT('这是演示4中的断言', data == data)


class case_5(object):
    name = '演示5'
    tags = ['ui测试']

    def setup(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示5的初始化,data:{data}')

    def teardown(self):
        # 用于单个用例的初始化操作
        data = GSTORE['data']
        INFO(f'这是演示5的清除操作,data:{data}')

    def teststeps(self):
        STEP(1, '第一步')
        data = GSTORE['data']
        INFO(f'这是演示5测试步骤中的data:{data}')
        CHECK_POINT('这是演示5中的断言', data == data)
