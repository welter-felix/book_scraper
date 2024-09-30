import scrapy
import logging

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            price = book.css('p.price_color::text').get().replace('£', '')
            price = float(price)
            availability = book.css('p.instock.availability::text').re_first('\\S+').strip()
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': price,
                'availability': availability
                
            }

        # Follow pagination link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            

    def errback(self, failure):
        # Log the error
        logging.error(repr(failure))