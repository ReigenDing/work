# -*- coding: utf-8 -*-
import scrapy
from gearbest.items import AppliancesItem


class AppliancesSpider(scrapy.Spider):
    name = 'appliances'
    allowed_domains = ['www.gearbest.com']
    start_urls = ['https://www.gearbest.com/appliances-c_12245/']

    def parse(self, response):
        link_list = response.xpath('.//div[@class="cateMain_asideItemBox"]/ul[@class="clearfix"]/li/a/@href').extract()
        print(len(link_list))
        for link in link_list:
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_appliances)
            # break

    # 提取appliances下分类的产品url
    def parse_appliances(self, response):
        global item
        item = AppliancesItem()
        # with open('./data.html', mode='w', encoding='utf-8') as fp:
        #     fp.write(response.text)
        link_list = response.xpath('.//div[@class="gbGoodsItem_outBox"]/p/a[@class="gbGoodsItem_title  "]/@href').extract()
        for link in link_list:
            print(link)
            item['product_url'] = link
            product_favorite = response.xpath('.//b[@class="goodsIntro_favCount"]/span[@class="js-favCount"]/text()').extract()
            print(product_favorite)
            yield scrapy.Request(url=link, callback=self.parse_product)
            # break

    # 提取单产品页面的信息
    def parse_product(self, response):
        product_name = response.xpath('//h1/text()').extract()[0].strip()
        print(product_name)
        product_sale_price = response.xpath('.//div[@class="goodsIntro_priceWrap"]/span/text()').extract()[0].strip()
        print(product_sale_price)
        product_comment = response.xpath('.//b[@class="goodsReviews_reviewNum"]/text()').extract()[0].strip()
        print(product_comment)
        product_pic_url = ','.join(response.xpath('.//div[@class="goodsIntro_thumbnail"]//span/img/@src').extract())
        print(product_pic_url)
        item['product_name'] = product_name
        item['product_sale_price'] = product_sale_price
        item['product_comment'] = product_comment
        item['product_pic_url'] = product_pic_url
        item['product_favorite'] = product_favorite
        yield item
