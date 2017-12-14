import scrapy

class LianjiaSpider (scrapy.Spider):
    name = "lianjia"
    def start_requests(self):
        urls=[
            'http://sh.lianjia.com/ershoufang/xuhui',
            'http://sh.lianjia.com/ershoufang/sh4731433.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page=response.url.split("/")[-2]
        filename = 'lianjia-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved file %s' % filename)