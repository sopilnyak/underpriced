import scrapy
import logging
import re

ATTRIBUTE_REPLACEMENT = {
    'Этаж': 'floor',
    'Общая площадь': 'area',
    'Площадь комнат': 'room_area',
    'Жилая площадь': 'living_area',
    'Площадь кухни': 'kitchen_area',
    'Совмещенных санузлов': 'combined_bathroom_count',
    'Раздельных санузлов': 'split_bathroom_count',
    'Вид из окна': 'view',
    'Балкон': 'balcony',
    'Ремонт': 'repair',
    'Тип дома': 'house_type',
    'Лифт': 'elevator',
    'Год постройки': 'construction_year',
    'Тип комнаты': 'room_type',
    'Высота потолков': 'ceiling_height',
    'Статус помещения': 'apartment_status',
    'Парковка': 'parking',
    'Пандус': 'ramp',
    'Кол-во спальных мест': 'sleeping_place_count'
}


class CianSpiderV2(scrapy.Spider):
    name = 'cian_spider_v2'

    def start_requests(self):
        start_price = 10000
        end_price = 200000
        price_step = 10000
        pattern = 'https://www.cian.ru/cat.php?deal_type=rent&engine_version=2' \
                  + '&offer_type=flat&quality=1&region=1&sort=id_user&type=4' \
                  + '&minprice={}&maxprice={}'
        for price in range(start_price, end_price, price_step):
            yield scrapy.Request(pattern.format(price, price + price_step - 1))

    def parse(self, response):
        for next_page in response.css('a.underground-header--A7XgS'):
            yield response.follow(next_page, self.parse_flat)

        for next_page in response.css('a.list-itemLink--39icE'):
            yield response.follow(next_page, self.parse)

    @staticmethod
    def cleanup_string(string):
        return string.replace('\xa0', ' ').replace('м2', '').strip()

    @staticmethod
    def fix_float(string):
        return string.replace(',', '.')

    def extract_flat_additional_data(self, response):
        attribute_names = map(
            lambda name: ATTRIBUTE_REPLACEMENT[name.strip()[:-1]],
            response.xpath('//table[@class="object_descr_props"]/tr/th/text()').extract()[1:]
        )
        attribute_values = map(
            lambda value: self.cleanup_string(value.xpath('string(.)').extract()[0]),
            response.xpath('//table[@class="object_descr_props"]/tr/td')
        )
        data = dict(zip(attribute_names, attribute_values))

        for field in ['area', 'living_area', 'kitchen_area']:
            if field in data:
                data[field] = self.fix_float(data[field])

        return data

    def extract_flat_price(self, response):
        extraction = response.xpath('//div[@class="object_descr_price"]/text()').extract()
        if len(extraction) == 0:
            return None
        line = extraction[0].strip()
        value = ''.join(re.findall(r'\d+', line))
        if 'руб' in line:
            return {
                'rub_price': value
            }
        elif '€' in line:
            return {
                'eur_price': value
            }
        elif '$' in line:
            return {
                'dol_price': value
            }
        logging.warning('Unknown price for line: %s', line)
        return None

    def extract_flat_rooms_count(self, response):
        extraction = response.xpath('//h2[@class="cf_sticky_head-head"]/text()').extract()
        if len(extraction) == 0:
            return None
        line = extraction[0].strip()
        value = line.split('-', 2)[0]
        return self.cleanup_string(value)

    def extract_flat_images(self, response):
        return response.xpath('//div[@class="fotorama"]/img/@src').extract()

    def extract_flat_description(self, response):
        extraction = response.xpath('//div[@class="object_descr_text"]/text()').extract()
        if len(extraction) == 0:
            return None
        return extraction[0].strip()

    def fix_flat_data(self, flat):
        flat['kitchen_area'].replace(',', '.')
        flat['living_area'].replace(',', '.')
        return flat

    def extract_flat_underground(self, response):
        underground_names = map(
            lambda name: name[:-1].strip(),
            response.xpath('//a[@class="object_item_metro_name"]/text()').extract()
        )
        distances = map(
            lambda distance: ' '.join(distance.split()),
            response.xpath('//span[@class="object_item_metro_comment"]/text()').extract()
        )
        return dict(zip(underground_names, distances))

    def extract_flat_district(self, response):
        district = re.search(r'<div class=\"bti__data__name\">Название<\/div>.*?<td>([^<]*)<\/td>', response.text, re.MULTILINE | re.S)
        if district is not None:
            return district.group(1)
        return ''

    def extract_flat_address(self, response):
        return ', '.join(response.xpath('//h1[@class="object_descr_addr"]/a/text()').extract()[-2:])

    def get_id(self, response):
        return response.url.rsplit('/', 2)[1]

    def parse_flat(self, response):
        if 'captcha' in response.url:
            return
        flat = dict()
        flat['url'] = response.url
        flat['_id'] = self.get_id(response)
        flat['price'] = self.extract_flat_price(response)
        flat['rooms'] = self.extract_flat_rooms_count(response)
        flat['images'] = self.extract_flat_images(response)
        flat['description'] = self.extract_flat_description(response)
        flat['underground'] = self.extract_flat_underground(response)
        flat['district'] = self.extract_flat_district(response)
        flat['address'] = self.extract_flat_address(response)
        flat.update(self.extract_flat_additional_data(response))
        if flat['price'] is not None and len(flat['underground']) > 0 and 'rub_price' in flat['price']:
            yield flat
