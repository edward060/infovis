import scrapy

class MathsItem(scrapy.Item):

    name = scrapy.Field()
    #课程url
    advisor = scrapy.Field()

    nationality = scrapy.Field()

    university = scrapy.Field()

    year = scrapy.Field()

    students = scrapy.Field()

    # url = scrapy.Field()

