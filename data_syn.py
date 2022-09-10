"""
数据同步程序入口
要求 Tushare 积分 2000 以上
"""

import argparse
from tables.stock_basic import stock_basic
from tables.trade_cal import trade_cal
from tables.name_change import name_change
from tables.hs_const import hs_const
from tables.stk_rewards import stk_rewards
from tables.bak_basic import bak_basic
from tables.daily import daily
from tables.weekly import weekly
from tables.monthly import monthly
from tables.money_flow import money_flow
from tables.stk_limit import stk_limit
from tables.money_flow_hsgt import money_flow_hsgt
from tables.hsgt_top10 import hsgt_top10
from tables.ggt_top10 import ggt_top10
from tables.ggt_daily import ggt_daily



# 全量历史初始化
def init():
    stock_basic.init()  # 沪深股票-基础信息-股票列表
    trade_cal.init()  # 沪深股票-基础信息-交易日历
    name_change.init()  # 沪深股票-基础信息-股票曾用名
    hs_const.init()  # 沪深股票-基础信息-沪深股通成份股
    stk_rewards.init()  # 沪深股票-基础信息-管理层薪酬和持股
    bak_basic.init()  # 沪深股票-基础信息-备用列表 （读取限制,每分钟调用2次）
    daily.init()  # 沪深股票-行情数据-A股日线行情
    weekly.init()  # 沪深股票-行情数据-A股周线行情
    monthly.init()  # 沪深股票-行情数据-A股月线行情
    money_flow.init()  # 沪深股票-行情数据-个股资金流向
    stk_limit.init()  # 沪深股票-行情数据-每日涨跌停价格
    money_flow_hsgt.init()  # 沪深股票-行情数据-沪深港通资金流向
    hsgt_top10.init()  # 沪深股票-行情数据-沪深股通十大成交股
    ggt_top10.init()  # 沪深股票-行情数据-港股通十大成交股
    ggt_daily.init()  # 沪深股票-行情数据-港股通每日成交统计



# 增量数据追加同步
def append():
    stock_basic.append()  # 沪深股票-基础信息-股票列表
    trade_cal.append()  # 沪深股票-基础信息-交易日历
    name_change.append()  # 沪深股票-基础信息-股票曾用名
    hs_const.append()  # 沪深股票-基础信息-沪深股通成份股
    stk_rewards.append()  # 沪深股票-基础信息-管理层薪酬和持股
    bak_basic.append()  # 沪深股票-基础信息-备用列表 （读取限制,每分钟调用2次）
    daily.append()  # 沪深股票-行情数据-A股日线行情
    weekly.append()  # 沪深股票-行情数据-A股周线行情
    monthly.append()  # 沪深股票-行情数据-A股月线行情
    money_flow.append()  # 沪深股票-行情数据-个股资金流向
    stk_limit.append()  # 沪深股票-行情数据-每日涨跌停价格
    money_flow_hsgt.append()  # 沪深股票-行情数据-沪深港通资金流向
    hsgt_top10.append()  # 沪深股票-行情数据-沪深股通十大成交股
    ggt_top10.append()  # 沪深股票-行情数据-港股通十大成交股
    ggt_daily.append()  # 沪深股票-行情数据-港股通每日成交统计


def use_age():
    print('Useage: python data_syn.py [--mode  init|append ]')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sync mode args')
    parser.add_argument("--mode", type=str, default='append', help='同步模式: init(初始化模式), append(增量追加模式)')
    args = parser.parse_args()
    mode = args.mode
    if mode == 'init':
        init()
    elif mode == 'append':
        append()
    else:
        use_age()
