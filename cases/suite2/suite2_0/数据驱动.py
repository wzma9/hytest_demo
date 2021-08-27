from hytest import *


class test_数据驱动(object):

    tags = ['接口测试']

    ddt_cases = [
            {
                'name': '数据驱动1',
                'para': [None, '88888888', '请输入用户名']
            },
            {
                'name': '数据驱动2',
                'para': ['user', None, '请输入密码']
            },
            {
                'name': '数据驱动3',
                'para': ['user', '88888888', '登录失败 : 用户名或者密码错误']
            }
        ]

    def teststeps(self):
        username, password, expected = self.para
        INFO(f'用户名：{username}  密码:{password}  expected:{expected}')
