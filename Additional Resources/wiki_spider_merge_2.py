import scrapy
import re
import unicodedata
import time


class WikiSpider(scrapy.Spider):

    name = "wiki_company_merge_2"

    def start_requests(self):
        parent = 'https://en.wikipedia.org/wiki/Cisco_Systems'
        yield scrapy.Request(url=parent, callback=self.parse)

        urls = ['https://en.wikipedia.org/wiki/Juniper_Networks',
                'https://en.wikipedia.org/wiki/Arista_Networks', 'https://en.wikipedia.org/wiki/Hewlett_Packard_Enterprise',
                'https://en.wikipedia.org/wiki/VMware', 'https://en.wikipedia.org/wiki/Huawei', 'https://en.wikipedia.org/wiki/D-Link',
                'https://en.wikipedia.org/wiki/Extreme_Networks', 'https://en.wikipedia.org/wiki/Big_Switch_Networks', 'https://en.wikipedia.org/wiki/Cumulus_Networks',
                'https://en.wikipedia.org/wiki/Dell_EMC', 'https://en.wikipedia.org/wiki/Lenovo', 'https://en.wikipedia.org/wiki/Mellanox_Technologies',
                'https://en.wikipedia.org/wiki/Netgear', 'https://en.wikipedia.org/wiki/Allied_Telesis', 'https://en.wikipedia.org/wiki/NEC',
                'https://en.wikipedia.org/wiki/ZTE']
        #url_2 = ['https://en.wikipedia.org/wiki/Cisco_Videoscape', 'https://en.wikipedia.org/wiki/Tandberg', 'https://en.wikipedia.org/wiki/Scientific_Atlanta']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        time.sleep(2)

        url_acquisition = ['https://en.wikipedia.org/wiki/List_of_acquisitions_by_Cisco_Systems']
        for acq in url_acquisition:
            yield scrapy.Request(url=acq, callback=self.acquisition_parse)

    def parse(self, response):

        def _clean(value):
            value = ' '.join(value)
            value = value.replace('\n', '')
            value = unicodedata.normalize("NFKD", value)
            value = re.sub(r' , ', ', ', value)
            value = re.sub(r' \( ', ' (', value)
            value = re.sub(r' \) ', ') ', value)
            value = re.sub(r' \)', ') ', value)
            value = re.sub(r'\[\d.*\]', ' ', value)
            value = re.sub(r' +', ' ', value)
            return value.strip()

        strings = []
        for i in range(0, 100):
            try:
                for node in response.xpath('//*[@id="mw-content-text"]/div/p[{}]'.format(i)):
                    text = _clean(node.xpath('string()').extract())
                    if len(text):
                        strings.append(text)
            except Exception as error:
                strings.append(str(error))

        info_card = dict()
        rows = response.xpath("//*[@id='mw-content-text']/div/table[contains(@class, 'infobox vcard')]/tbody/tr")

        for row in rows:
            # Scraping info box values
            if row.xpath('th'):
                item = row.xpath('th//text()').extract()
                item = [_.strip() for _ in item if _.strip() and _.replace('\n', '')]
                item = ' '.join(item)
                item = item.replace('\n', '')
                item = unicodedata.normalize("NFKD", item)
                item = re.sub(r' +', ' ', item)
                item = item.strip()

                if row.xpath('td/div/ul/li'):
                    value = []
                    for li in row.xpath('td/div/ul/li'):
                        value.append(''.join(li.xpath('.//text()').extract()))
                    value = [_.strip() for _ in value if _.strip() and _.replace('\n', '')]
                    value = ', '.join(value)
                else:
                    value = row.xpath('td//text()').extract()
                    value = [_.strip() for _ in value if _.strip() and _.replace('\n', '')]

                    if item == 'Website':
                        value = ''.join(value)
                    else:
                        value = ' '.join(value)

                value = value.replace('\n', '')
                value = unicodedata.normalize("NFKD", value)
                value = re.sub(r' , ', ', ', value)
                value = re.sub(r' \( ', ' (', value)
                value = re.sub(r' \) ', ') ', value)
                value = re.sub(r' \)', ') ', value)
                value = re.sub(r'\[\d\]', ' ', value)
                value = re.sub(r' +', ' ', value)
                value = value.strip()
                info_card[item] = value

        rows = response.xpath("//*[@id='mw-content-text']/div/table[contains(@class, 'wikitable')]/tbody/tr")
        table = {}
        #for row in rows:
            #columns = row.css('td')
            #if len(columns) == 6:
                #year = columns[0].css('::text').extract_first()
                #rev_mil = columns[1].css('::text').extract_first()
                #income_mil = columns[2].css('::text').extract_first()
                #assets_mil = columns[3].css('::text').extract_first()
                #share_price = columns[4].css('::text').extract_first()
                #employees = columns[5].css('::text').extract_first()

                #table['year'] = year.strip()
                #table['rev_mil'] = rev_mil.strip()
                #table['income_mil'] = income_mil.strip()
                #table['assets_mil'] = assets_mil.strip()
                #table['share_price'] = share_price.strip()
                #table['employees'] = employees.strip()

                #yield {
                #   ** table
                #}
            # elif len(columns) == 2:
            # technology = columns[0].css('::text').extract_first()
            # product_family = columns[1].css('::text').extract_first()

            # table['Technology'] = technology.strip()
            # table['Product_family'] = product_family.strip()

            # yield{
            #    **table
            # }

        yield {
            'Title': response.css('#firstHeading::text').extract_first(),
            'Organization_name': response.css('#mw-content-text > div >'
                                              ' table.infobox.vcard > caption::text').extract_first(),
            **info_card,
            'strings': strings,
        }

        return table

    def acquisition_parse(self, response):

        rows = response.xpath("//*[@id='mw-content-text']/div/table[contains(@class, 'wikitable sortable')]/tbody/tr")
        table_2 = {}

        for row in rows:
            columns = row.css('td')
            if len(columns) == 7:
                acquired_on = columns[1].css('::text').extract_first()
                company = columns[2].css('::text').extract_first()
                business = columns[3].css('::text').extract_first()
                value = columns[5].css('::text').extract_first()

                table_2['acquired_on'] = acquired_on.strip()
                table_2['company'] = company.strip()
                table_2['business'] = business.strip()
                table_2['value'] = value.strip()

                #if company == 'NDS Group' or company == 'Scientific-Atlanta' or company == 'Tandberg':
                #    count = 0
                #    for next_page in row.css('td > a'):
                #        if count < 1:
                #            yield response.follow(next_page, self.parse)
                #            count += 1

                yield{
                    **table_2
                }

        return table_2


