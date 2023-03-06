import scrapy


class MaginonCrawlerSpider(scrapy.Spider):
    name = "maginon_crawler"
    allowed_domains = ["maginon.de"]
    start_urls = ["http://maginon.de"]

    custom_settings = {
        'FEEDS': {
            'output.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        },
    }

    def parse(self, response):
        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            if '/collections/' in link:
                category_name = link.split('/')[-1]
                print(category_name)
                yield response.follow(link, callback=self.parse_collection, meta={'category': category_name})

    def parse_collection(self, response):
        print('i am at products')
        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            if '/products/' in link:
                model_name = link.split('/')[-1]
                category_name = response.meta['category']

                product_data = {
                'model': model_name,
                'category': category_name
                }
            
                yield product_data
                

        
        
        # print(response)
        

                
        
  
    
 
