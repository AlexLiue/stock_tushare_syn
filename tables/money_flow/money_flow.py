"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2022/9/10 08:18
# @Author  : PcLiu
# @FileName: money_flow.py
===========================

接口：money_flow，可以通过数据工具调试和查看数据。
描述：获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向
限量：单次最大提取5000行记录，总量不限制
积分：用户需要至少2000积分才可以调取，基础积分有流量控制，积分越多权限越大，请自行提高积分，具体请参阅积分获取办法
tushare 接口说明：https://tushare.pro/document/2?doc_id=170
"""


import os
import time
import datetime
from utils.utils import exec_mysql_script, get_tushare_api, get_mock_connection, get_logger


# 全量初始化表数据
def init():
    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    exec_mysql_script(dir_path)
    start_date = '20070101'  # tushare 仅包含 2007 年后的数据
    now = datetime.datetime.now()
    end_date = now.strftime('%Y%m%d')
    exec_syn(trade_date='', start_date=start_date, end_date=end_date, interval=0)


# 增量追加表数据
def append():
    now = datetime.datetime.now()
    date = now.strftime('%Y%m%d')
    exec_syn(trade_date=date, start_date='', end_date='', interval=0)


# trade_date: 交易日期, 空值时匹配所有日期 (增量单日增加参数)
# start_date: 数据开始日期（全量历史初始化参数）
# end_date: 数据结束日期（全量历史初始化参数）
# interval: 每次拉取的时间间隔
def exec_syn(trade_date, start_date, end_date, interval):
    ts_api = get_tushare_api()
    connection = get_mock_connection()
    logger = get_logger('money_flow', 'data_syn.log')

    if trade_date != '':
        start_date = trade_date
        end_date = trade_date

    # 考虑到单次仅能读取5000条记录, 且不存在偏移查询机制, 一次仅查询一天所有股票的数据, 因此按天查询
    start = datetime.datetime.strptime(start_date, '%Y%m%d')
    end = datetime.datetime.strptime(end_date, '%Y%m%d')
    while start <= end:
        start += datetime.timedelta(days=1)
        date = str(start.strftime('%Y%m%d'))

        logger.info("Query money_flow from tushare with api[moneyflow] trade_date[%s]" % date)

        data = ts_api.moneyflow(**{
            "trade_date": date
        }, fields=[
            "ts_code",
            "trade_date",
            "buy_sm_vol",
            "buy_sm_amount",
            "sell_sm_vol",
            "sell_sm_amount",
            "buy_md_vol",
            "buy_md_amount",
            "sell_md_vol",
            "sell_md_amount",
            "buy_lg_vol",
            "buy_lg_amount",
            "sell_lg_vol",
            "sell_lg_amount",
            "buy_elg_vol",
            "buy_elg_amount",
            "sell_elg_vol",
            "sell_elg_amount",
            "net_mf_vol",
            "net_mf_amount"
        ])
        logger.info('Write [%d] records into table [money_flow] with [%s]' % (data.iloc[:, 0].size, connection.engine))
        data.to_sql('money_flow', connection, index=False, if_exists='append', chunksize=5000)

        time.sleep(interval)


if __name__ == '__main__':
    append()

