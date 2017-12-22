-- 公司基本信息表
DROP TABLE IF EXISTS t_company_fundamental;
CREATE TABLE t_company_fundamental(
    company_fundamental_key_id int(30) NOT NULL AUTO_INCREMENT,
    ticker varchar(50)                                    comment  '老式股票收报机，目前指股票标的',
    company_name VARCHAR(200),
    sector VARCHAR(100)                                   comment  '所属行业大类',
    industry VARCHAR(200)                                 comment  '所属行业子类',
    country VARCHAR(100),
    market_cap VARCHAR(100)                               comment  '市值',
    price_earnings_ratio VARCHAR(100) comment'市盈率',
    price varchar(100),
    price_change varchar(100),
    volume varchar(100),
    primary key (company_fundamental_key_id)
)ENGINE=InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET= utf8;



-- 分析师行动
DROP TABLE IF EXISTS t_analyst_action;
CREATE TABLE t_analyst_action(
    analyst_action_key_id int(30) NOT NULL AUTO_INCREMENT,
    ticker varchar(50),
    investment_bank varchar(100) comment '投行',
    action_date varchar(50)      comment '行动日期',
    action_overview varchar(100)  comment '行动概览',
    action_grade_detail varchar(100)    comment '行动级明细',
    action_price_detail varchar(100)    comment '行动价格明细',
    primary key (analyst_action_key_id)

)ENGINE=InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET= utf8;
