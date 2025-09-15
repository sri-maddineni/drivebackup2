import scrapy
from ..items import Pro1Item


class Quotesspy(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/"]

    # mandatory variable
    pn=2

    def parse(self, response):
        x = Pro1Item()

        adq = response.css('div.quote')

        for q in adq:
            # title = response.css('title::text').extract_first()
            title = q.css("span.text::text").extract()
            author = q.css('.author::text').extract()

            x['title'] = title
            x['author'] = author

            yield x

        np = "https://quotes.toscrape.com/page/"+str(self.pn)+"/"

        if self.pn<=11:
            # goto next
            yield response.follow(np, callback=self.parse)
            self.pn+=1
