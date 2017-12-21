import mysql.connector
import scrapy
from scrapy_splash import SplashRequest


class WBSpider(scrapy.Spider):
    name = "finviz"
    start_urls = [
        'https://finviz.com/screener.ashx?v=111&f=cap_midover'
    ]

    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }





    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], headers=self.headers,  args={'wait': 3})







    def parse(self, response):
        conn = mysql.connector.connect(user='root', password='root', database='stock_db')
        cursor = conn.cursor()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫开始+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        companyList = response.xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table/tbody/tr[position()>1]')

        list2 = []
        for company in companyList:
            fundamentals = company.xpath('./td[position()>1]')
            list1 = []
            for fundamental in fundamentals:
                item = fundamental.xpath('./a/text()').extract_first()
                list1.append(item)

            list2.append(list1)

            # cursor.execute('insert into t_text(name, content) VALUES (%s, %s)', ['梁斌penny', y.strip()])

        print(list2)

        conn.commit()
        cursor.close()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫结束+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

