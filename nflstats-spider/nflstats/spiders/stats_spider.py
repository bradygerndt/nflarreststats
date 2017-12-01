import scrapy
import re
import lxml
import time

class StatsSpider(scrapy.Spider):
    name ="stats"

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
    }

   

    
    def start_requests(self):
        teams = ['crd', 'nwe', 'buf', 'mia', 'nyj', 'pit', 'rav', 'cin', 'cle', 'oti', 'jax', 'htx', 'clt', 'kan', 'rai', 'sdg', 'den', 'phi', 'dal', 'was', 'nyg', 'min', 'gnb', 'det', 'chi', 'nor', 'car', 'atl', 'tam', 'ram', 'sea', 'sfo']


        for team in teams:
            for i in range(2000, 2014):
                currentUrl =  'https://www.pro-football-reference.com/teams/' + team + '/' + str(i) + '_roster.htm'
                yield scrapy.Request(url=currentUrl, callback=self.parse, errback=self.errReport, meta={'team': team, 'year': i })

    def getData(self, row, file, team, year):
        #print('----- New Row -----\n')
        #print(str(len(row)) + ' items in this row')
        for item in row:
            #if item.attrib['data-stat'] == None:
            file.write("\"" + item.text_content() + "\",")
            #print(item.attrib['data-stat'] + ' is type: ' + str(type(item.attrib['data-stat'] )) + " : " + item.text_content())
            #print(item.attrib['data-stat'] ' : ' + item.text_content())
        file.write(',' + team + ',' + str(year) + '\n')
            
    def parse(self, response):
        team = response.meta.get('team')
        year = response.meta.get('year')

        commentedRes = (response.xpath('//*[@id="all_games_played_team"]/comment()').extract())
        resRe = re.split('[<\n\s\][!.]--[\n.>]', commentedRes[0])
        resFixed = lxml.html.fromstring(resRe[1])
        print('----------Getting roster for ' + str(year) +' ' + team + '--------------- \n')
        with open('new_dudes.csv', 'a') as f:
            [self.getData(row, f, team, year) for row in resFixed.xpath('//tbody/tr')]
    
    def errReport(self, response):
        team = response.meta.get('team')
        year = response.meta.get('year')
        print('Error processing ' + team + ' for' + str(year))
        with open('errlog.log', 'a') as f:
            f.write('Error processing ' + team +' for' + str(years) + '\n')
        
  