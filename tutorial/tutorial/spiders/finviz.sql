-- 公司基本信息表
DROP TABLE IF EXISTS t_company_fundamental;
CREATE TABLE t_company_fundamental(
    company_fundamental_key_id int(11) NOT NULL AUTO_INCREMENT,
    ticker varchar(50),
    company_name VARCHAR(200),
    sector VARCHAR(100) comment'所属行业大类',
    industry VARCHAR(200) comment'所属行业子类',
    country VARCHAR(100),
    market_cap VARCHAR(100) comment'市值',


)