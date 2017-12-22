import mysql.connector
import scrapy
from scrapy_splash import SplashRequest


# 市值大于2B 的公司数据
class StockSpider(scrapy.Spider):
    name = "finviz"
    origin_url = 'https://finviz.com/'

    start_urls = [
        'https://finviz.com/screener.ashx?v=111&f=cap_midover'
    ]

    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    #
    # def generate_urls(self):
    #     start_url = self.origin_url+'screener.ashx?v=111&f=cap_midover&r='
    #     for i in range(1,89):
    #         start_url += i*20+1
    #         self.start_urls.append(start_url)





    def start_requests(self):
        for i in range(1,89):
            start_url = self.origin_url+'screener.ashx?v=111&f=cap_midover&r='
            start_url += str(i*20+1)
            self.start_urls.append(start_url)
        for url in self.start_urls:
            yield SplashRequest(url=url, headers=self.headers,  args={'wait': 10})







    def parse(self, response):
        conn = mysql.connector.connect(user='root', password='root', database='stock_db')
        cursor = conn.cursor()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫开始+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        companyList = response.xpath('//*[@id="screener-content"]/table/tbody/tr[4]/td/table/tbody/tr[position()>1]')

        sql = 'insert into t_company_fundamental(ticker, company_name, sector, industry, country, market_cap, price_earnings_ratio, price, price_change, volume) VALUES'
        list2 = []
        for company in companyList:
            fundamentals = company.xpath('./td[position()>1]')
            list1 = []
            for fundamental in fundamentals:
                item = fundamental.xpath('./a/text()').extract_first()
                if(item==None):
                    item = fundamental.xpath('./a/span/text()').extract_first()
                list1.append(item)

            sql+='(\"'+list1[0]+'\", \"'+list1[1]+'\", \"'+list1[2]+'\", \"'+list1[3]+'\", \"'+list1[4]+'\", \"'+list1[5]+'\", \"'+list1[6]+'\", \"'+list1[7]+'\", \"'+list1[8]+'\", \"'+list1[9]+'\"), '

            list2.append(list1)

        print(sql[0:sql.__len__()-2])
        cursor.execute(sql[0:sql.__len__()-2])



        conn.commit()
        cursor.close()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫结束+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")






start_url = 'screener.ashx?v=111&f=cap_midover&r='
for i in range(1,89):
    start_url = 'screener.ashx?v=111&f=cap_midover&r='
    start_url += str(i*20+1)
    print(start_url)