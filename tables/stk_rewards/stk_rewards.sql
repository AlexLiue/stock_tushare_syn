-- stock.stk_rewards definition

DROP TABLE IF EXISTS `stk_rewards`;
CREATE TABLE `stk_rewards`
(
    `id`       bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
    `ts_code`  varchar(16) DEFAULT NULL COMMENT 'TS股票代码',
    `ann_date` date        DEFAULT NULL COMMENT '公告日期',
    `end_date` date        DEFAULT NULL COMMENT '截止日期',
    `name`     varchar(64) DEFAULT NULL COMMENT '姓名',
    `title`    varchar(64) DEFAULT NULL COMMENT '职务',
    `reward`   double      DEFAULT NULL COMMENT '报酬',
    `hold_vol` double      DEFAULT NULL COMMENT '持股数',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='管理层薪酬和持股';