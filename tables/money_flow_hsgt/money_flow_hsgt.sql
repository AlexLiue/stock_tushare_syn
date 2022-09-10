-- stock.money_flow_hsgt definition

DROP TABLE IF EXISTS `money_flow_hsgt`;
CREATE TABLE `money_flow_hsgt`
(
    `id`          bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
    `trade_date`  date   DEFAULT NULL COMMENT '交易日期',
    `ggt_ss`      double DEFAULT NULL COMMENT '港股通（上海）',
    `ggt_sz`      double DEFAULT NULL COMMENT '港股通（深圳）',
    `hgt`         double DEFAULT NULL COMMENT '沪股通（百万元）',
    `sgt`         double DEFAULT NULL COMMENT '深股通（百万元）',
    `north_money` double DEFAULT NULL COMMENT '北向资金（百万元）',
    `south_money` double DEFAULT NULL COMMENT '南向资金（百万元）',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='沪深股票-行情数据-沪深港通资金流向';