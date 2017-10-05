import scrapy
#引入容器
from Maths.MathsItems import MathsItem

class MySpider(scrapy.Spider):
    #设置name
    name = "MySpider"
    #设定域名
    allowed_domains = ["genealogy.math.ndsu.nodak.edu"]
    #填写爬取地址
    start_urls = ["https://www.genealogy.math.ndsu.nodak.edu/id.php?id=7378"]
    #编写爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        item = MathsItem()
        #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #先获取每个课程的div
        for box in response.xpath('//div[@id="paddingWrapper"]'):
            #获取每个div中的课程路径
            item['name'] = box.xpath('.//h2/text()').extract()[0].strip()
            #获取div中的课程标题
            item['advisor'] = box.xpath('.//p[2]/a/text()').extract()[0]

            item['nationality'] = box.xpath('.//img/@title').extract()[0]

            item['university'] = box.xpath(".//span/text()").extract()[1]

            item['year'] = box.xpath(".//span/text()").extract()[2]

            item['students'] = box.xpath('.//table/tr/td/a/text()').extract()

            # item['url'] = box.xpath('.//table/tr/td/a/@href').extract()
            yield item


        # url跟进开始
        # 获取下一页的url信息
        url = box.xpath('.//table/tr/td/a/@href').extract()
        for item in url:
            # 将信息组合成下一页的url
            page = 'https://www.genealogy.math.ndsu.nodak.edu/' + item
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
            break

        # url跟进结束

