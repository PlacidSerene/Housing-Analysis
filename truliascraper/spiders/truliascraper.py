import scrapy

class truliaSpider(scrapy.Spider):
    name = 'trulia'
    # start_urls = ['https://www.trulia.com/CA/Sacramento/']

    # allowed_domains = ['https://www.trulia.com/']

    start_urls = ['https://www.trulia.com/CA/Sacramento/']
    # start_urls = [base_url+str(i)+'_p/' for i in range(1,29)]

    # def start_requests(self):
    #     base_url = 'https://www.trulia.com/CA/Sacramento/'
    #     urls = [base_url+str(i)+'_p/' for i in range(1,29)]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)   

    def parse(self, response):
        for link in response.css('a.PropertyCard__StyledLink-m1ur0x-3.dgzfOv'):
            url = 'trulia.com' + link.css('a::attr(href)').get()
            # print(url)
            yield response.follow(url, callback=self.parse_information)
            # yield {
            #     'url': url
            # }


    def parse_information(self, response):
        
        yield {
            "address": response.css('span.Text__TextBase-sc-1cait9d-0.ifMipu::text').get(),
            "zip_code": response.css('span.Text__TextBase-sc-1cait9d-0.cZbUGb.HomeSummaryShared__ CityStateAddress-mmeem6-0.dBjJRw::text').get().replace('Sacramento, CA ',''),
            "bed": response.css('div.MediaBlock__MediaContent-skmvlj-1.gnreBg::text').getall()[0],
            "ba": response.css('div.MediaBlock__MediaContent-skmvlj-1.gnreBg::text').getall()[1],
            "sqft": response.css('div.MediaBlock__MediaContent-skmvlj-1.gnreBg::text').getall()[2],
            'year_built': response.css('span.Feature__FeatureListItem-sc-8qiunc-0.kLjNvv::text').getall()[1],
            'lot_sqft': response.css('span.Feature__FeatureListItem-sc-8qiunc-0.kLjNvv::text').getall()[-1],
            'price': response.css('div.Text__TextBase-sc-1cait9d-0-div.Text__TextContainerBase-sc-1cait9d-1.nBoMt::text').get()
        }











        # for house in response.css('div.Box__BoxElement-sc-1f5rw0h-0.bsjsJO.PropertyCard__PropertyCardContainer-m1ur0x-4.faCQjz'):
            
            # yield {
            # 'price': house.css('div.Text__TextBase-sc-1cait9d-0-div.Text__TextContainerBase-sc-1cait9d-1.keMYfJ::text').get().replace('$',''),
            # 'bd&ba': house.css('div.Text__TextBase-sc-1cait9d-0-div.Text__TextContainerBase-sc-1cait9d-1.bjqKkI::text').getall(),
            # 'sqft': house.css('div.Text__TextBase-sc-1cait9d-0-div.Text__TextContainerBase-sc-1cait9d-1.dZyoXR::text').get().replace(' sqft',''),
            # 'address': house.css('a.PropertyCard__StyledLink-m1ur0x-3.dgzfOv div.Text__TextBase-sc-1cait9d-0-div.Text__TextContainerBase-sc-1cait9d-1.dZyoXR::text').getall()
            #     }
        #     except:
        #         yield {
        #             'price': None,
        #             'bed': None,
        #             'ba': None,
        #             'sqft': None
        #         }

        # next_page = response.css('a.ButtonBase-sc-14ooajz-0.PrimaryButton-sc-16zopmz-0.PaginationButton__PaginationCarouselButton-sc-1yuoxn6-0.gkxBov::attr(href)').get()
        # print(next_page)
        # if next_page is not None:
        #     # print('This is the next page: ', next_page)
        #     yield response.follow('https://www.trulia.com'+next_page, callback=self.parse)
    # def parse_additional_data(self, response):
