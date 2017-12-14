import scrapy
from scrapy.conf import settings
from scrapy_splash import SplashRequest
import mysql.connector



class WBSpider(scrapy.Spider):
    name = "wb"
    start_urls = [
        'https://weibo.com/pennyliang?from=myfollow_all&is_all=1#1512796955702'
    ]


    cookie = settings['COOKIE']

    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }





    # 每页有三段信息，默认展示第一段，下拉滚动调用url展示第二第三段
    loading_url =  "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&from=page_100505&mod=TAB&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__22&id=1005051497035431&script_uri=/p/1005051497035431/home&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1513178655243"





    def start_requests(self):
        yield SplashRequest(url=self.loading_url, headers=self.headers, cookies=self.cookie,  args={'wait': 5})

    def start_requests(self):
        # yield scrapy.Request(url=self.start_urls[0], headers=self.headers, cookies=self.cookie)
        yield SplashRequest(url=self.start_urls[0], headers=self.headers, cookies=self.cookie,  args={'wait': 5})







    def parse(self, response):
        conn = mysql.connector.connect(user='root', password='root', database='wb')
        cursor = conn.cursor()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫开始+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        a = response.xpath('//*[@class="WB_text W_f14"]')
        for x in a:
            y = x.xpath('./text()').extract_first()
            print(y.strip())
            cursor.execute('insert into t_text(name, content) VALUES (%s, %s)', ['梁斌penny', y.strip()])


        conn.commit()
        cursor.close()

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++爬虫结束+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

