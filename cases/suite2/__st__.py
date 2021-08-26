from hytest import *
from lib.get_time import *


def suite_setup():
    data2 = time_stamp
    GSTORE['data2'] = data2
    INFO(f'suite2的初始化,data={GSTORE["data2"]}')
