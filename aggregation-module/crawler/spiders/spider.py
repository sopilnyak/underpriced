import scrapy
import re

URLS = ['https://www.cian.ru/', 'https://kvadroom.ru/',
'https://realty.yandex.ru/']

class CianSpider(scrapy.Spider):
    name = 'cian_spider'
    start_urls = ['https://www.cian.ru/snyat-kvartiru/']

    def parse(self, response):
        filename = 'cian.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log('Saved file %s' % filename)
        yield self.parse_details(response)
        pages = response.css('div.container--1LvHI ul.list--35Suf').css('li.list-item--2QgXB')
        for page in pages:
            li = page.css('li.list-item--2QgXB')
            if len(li.css('a')) == 0:
                continue
            if li.css('a::text') == '..':
                break
            link = li.css('a::attr(href)').extract()[0]
            if link is not None:
                yield scrapy.Request(link, callback=self.parse_details)

    def parse_details(self, response):
        flats = []
        flats_descriptions = response.css('div.wrapper--1Z8Nz div.offer-container--38nzf')
        for flat_descr in flats_descriptions:
            flat = self.extract_features_per_flat(flat_descr)
            flats.append(flat)
        return flats

    def extract_address(self, flat_descr):
        address_lines = flat_descr.css('div.address-path--12tl2 a')
        address = ''
        for line in address_lines:
            address = address + line.css('a::text').extract()[0] + ' '
        return re.sub(r'(\xa0)', '', address[:-1])

    # Sometimes it's only 'Moscow'
    def extract_underground(self, flat_descr):
        underground = flat_descr.css('div.underground--2Yfq9 a::text').extract()
        if len(underground) > 0:
            return underground[0]
        else:
            return None

    def extract_underground_distance(self, flat_descr):
        item = flat_descr.css('div.underground--2Yfq9 div.underground-distance--1NsmB::text').extract()
        if len(item) > 0:
            item = re.sub('\xa0', ' ', item[0])
            pattern = re.compile(r'([<>]|)([0-9]+)(.*)')
            return int(pattern.findall(item)[0][1])
        else:
            return None

    def extract_price(self, flat_descr):
        price_descr = flat_descr.css('div.column--3zb_O div.header--2lxlC::text').extract()[0]
        return int(''.join(price_descr.split(' ')[:-1]))

    def extract_comission(self, flat_descr):
        comission = flat_descr.css('div.column--3zb_O div.term--34Es8::text').extract()
        return False if u'без комиссии' in comission else True

    def extract_rooms(self, flat_descr):
        rooms = flat_descr.css('div.column--3zb_O div.header--NemOm::text').extract()[0]
        if rooms == u'Студия':
            return -1
        if rooms == u'Многокомнатная':
            return 10
        return int(rooms.split('-')[0])

    def extract_areas(self, flat_descr):
        total = None
        kitchen = None
        living = None
        total = float(flat_descr.css('div.column--3zb_O div.header--1WFWC::text').extract()[0].split(' ')[0])
        sub_areas = flat_descr.css('div.column--3zb_O div.term--2RMqZ::text').extract()
        if len(sub_areas) > 0:
            if len(sub_areas) == 1:
                items = sub_areas[0].split(' ')
                if u'кухня' in items:
                    kitchen = float(items[1])
                else:
                    living = float(items[1])
            if len(sub_areas) == 2:
                kitchen = float(sub_areas[0].split(' ')[1])
                living = float(sub_areas[1].split(' ')[1])
        return (total, kitchen, living)

    def extract_floors(self, flat_descr):
        floors = flat_descr.css('div.column--3zb_O div.header--1ZTfS::text').extract()[0].split(' ')
        current = int(floors[0])
        total = int(floors[3])
        return (current, total)

    def extract_id(self, flat_descr):
        pattern = re.compile(r'(.*)/([0-9]*)/(.*)')
        a_item = flat_descr.css('div.content-footer--20Yyt a').extract()[0]
        id = int(pattern.findall(a_item)[0][1])
        return id

    def extract_image(self, flat_descr):
        img_link = flat_descr.css('div.container--C5wLT img::attr(src)').extract()
        if len(img_link) > 0:
            return img_link[0]
        else:
            return None

    def extract_features_per_flat(self, flat_descr):
        flat_features = {}

        flat_features['address'] = self.extract_address(flat_descr)

        flat_features['underground'] = self.extract_underground(flat_descr)

        # time in minutes
        flat_features['underground_distance'] = self.extract_underground_distance(flat_descr)

        flat_features['price'] = self.extract_price(flat_descr)

        flat_features['is_commission'] = self.extract_comission(flat_descr)

        # МНОГОКОМНАТНАЯ!
        flat_features['rooms_number'] = self.extract_rooms(flat_descr)

        # (total, kitchen, for living)
        flat_features['areas'] = self.extract_areas(flat_descr)

        # (current/total)
        flat_features['floors'] = self.extract_floors(flat_descr)

        flat_features['id'] = self.extract_id(flat_descr)

        flat_features['image'] = self.extract_image(flat_descr)

        return flat_features
