from hytest import *


class case_11(object):
    name = '演示11'
    tags = ['接口测试']

    def teststeps(self):
        INFO('这是演示11')
        CHECK_POINT('断言11', 'hello' in 'hello world')
