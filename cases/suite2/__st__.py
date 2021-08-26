from hytest import *


def suite_setup():
    GSTORE['data'] = 0
    INFO(f'suite2的初始化,data={GSTORE["data"]}')
