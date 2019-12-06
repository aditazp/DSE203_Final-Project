import time
import csv
from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys

page_urls = ["https://www.crunchbase.com/organization/cisco", "https://www.crunchbase.com/organization/juniper-networks"
             , "https://www.crunchbase.com/organization/arista-networks", "https://www.crunchbase.com/organization/hewlett-packard"]

Dic = ['cisco.txt', 'juniper.txt', 'arista.txt', 'hewlett.txt']

driver = webdriver.Chrome('/Users/erikhoye/Desktop/Data_Integration_Final_Project/wikepedia_webscrapper/wikepedia_webscrapper/chromedriver')

company_num = 0
for page in page_urls:
    MyDicts = {}
    try:
        driver.get(page)
        time.sleep(4)

        c1 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[1]/label-with-info/span/span[2]/span").text
        c2 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[2]/field-formatter/identifier-multi-formatter/span").text
        vars()[c1] = c2

        c3 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[3]/label-with-info/span/span[2]/span").text
        c4 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[4]/field-formatter/identifier-multi-formatter/span").text
        vars()[c3] = c4

        c5 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[5]/label-with-info/span/span[2]/span").text
        c6 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[6]/field-formatter/span").text
        vars()[c5] = c6

        c7 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[7]/label-with-info/span/span[2]/span").text
        c8 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[8]/field-formatter/identifier-multi-formatter/span").text
        vars()[c7] = c8

        c9 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[9]/label-with-info/span/span[2]/span").text
        c10 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[10]/field-formatter/span").text
        c9 = 'Operating_' + c9
        vars()[c9] = c10

        c11 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[11]/label-with-info/span/span[2]/span").text
        c12 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[12]/field-formatter/span").text
        c11 = 'Funding_' + c11
        vars()[c11] = c12

        if company_num < 3:
            c13 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[15]/label-with-info/span/span[2]/span").text
            c14 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[16]/field-formatter/a").text
            vars()[c13] = c14
        else:
            c13 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[13]/label-with-info/span/span[2]/span").text
            c14 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[14]/field-formatter/a").text
            vars()[c13] = c14

        if company_num < 1:
            for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees'):
                MyDicts[i] = locals()[i]

        else:
            c15 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[1]/label-with-info/span/span[1]").text
            c16 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[2]/field-formatter/link-formatter/a").text
            vars()[c15] = c16

            c17 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[3]/label-with-info/span/span[1]").text
            c18 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[4]/field-formatter/span").text
            c17 = c17.replace(" ", "_")
            c17 = c17 + "_IPO"
            vars()[c17] = c18

            c19 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[5]/label-with-info/span/span[1]").text
            c20 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[6]/field-formatter/span").text
            c19 = c19.replace(" ", "_")
            c19 = c19 + "_IPO"
            vars()[c19] = c20

            if company_num != 2:
                c21 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[7]/label-with-info/span/span[1]").text
                c22 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[8]/field-formatter/span").text
                c21 = c21.replace(" ", "_")
                c21 = c21 + "_Price"
                vars()[c21] = c22

                c23 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[9]/label-with-info/span/span[1]").text
                c24 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[10]/field-formatter/span").text
                c23 = c23.replace(" ", "_")
                c23 = c23 + "_Date"
                vars()[c23] = c24

                for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees', 'Stock', 'Valuation_at_IPO',
                          'Money_Raised_at_IPO', 'IPO_Share_Price', 'IPO_Date'):
                    MyDicts[i] = locals()[i]

            else:
                c21 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[7]/label-with-info/span/span[1]").text
                c22 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[8]/field-formatter/span").text
                c21 = 'IPO_' + c21
                vars()[c21] = c22

                for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees', 'Stock', 'Valuation_at_IPO',
                          'Money_Raised_at_IPO', 'IPO_Date'):
                    MyDicts[i] = locals()[i]

        outputFile = open(Dic[company_num], "w")
        outputFile.write(str(MyDicts))
        outputFile.flush()
        outputFile.close()

    except:
        print('In Exception')
        driver.get(page)
        time.sleep(10)

        c1 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[1]/label-with-info/span/span[2]/span").text
        c2 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[2]/field-formatter/identifier-multi-formatter/span").text
        vars()[c1] = c2

        c3 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[3]/label-with-info/span/span[2]/span").text
        c4 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[4]/field-formatter/identifier-multi-formatter/span").text
        vars()[c3] = c4

        c5 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[5]/label-with-info/span/span[2]/span").text
        c6 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[6]/field-formatter/span").text
        vars()[c5] = c6

        c7 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[7]/label-with-info/span/span[2]/span").text
        c8 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[8]/field-formatter/identifier-multi-formatter/span").text
        vars()[c7] = c8

        c9 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[9]/label-with-info/span/span[2]/span").text
        c10 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[10]/field-formatter/span").text
        c9 = 'Operating_' + c9
        vars()[c9] = c10

        c11 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[11]/label-with-info/span/span[2]/span").text
        c12 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[12]/field-formatter/span").text
        c11 = 'Funding_' + c11
        vars()[c11] = c12

        if company_num < 3:
            c13 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[15]/label-with-info/span/span[2]/span").text
            c14 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[16]/field-formatter/a").text
            vars()[c13] = c14
        else:
            c13 = driver.find_element_by_xpath("//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[13]/label-with-info/span/span[2]/span").text
            c14 = driver.find_element_by_xpath( "//*[@id='section-overview']/mat-card/div[2]/fields-card[1]/div/span[14]/field-formatter/a").text
            vars()[c13] = c14

        if company_num < 1:
            for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees'):
                MyDicts[i] = locals()[i]

        else:

            c15 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[1]/label-with-info/span/span[1]").text
            c16 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[2]/field-formatter/link-formatter/a").text
            vars()[c15] = c16

            c17 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[3]/label-with-info/span/span[1]").text
            c18 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[4]/field-formatter/span").text
            c17 = c17.replace(" ", "_")
            c17 = c17 + "_IPO"
            vars()[c17] = c18

            c19 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[5]/label-with-info/span/span[1]").text
            c20 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[6]/field-formatter/span").text
            c19 = c19.replace(" ", "_")
            c19 = c19 + "_IPO"
            vars()[c19] = c20

            if company_num != 2:
                c21 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[7]/label-with-info/span/span[1]").text
                c22 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[8]/field-formatter/span").text
                c21 = c21.replace(" ", "_")
                c21 = c21 + "_Price"
                vars()[c21] = c22

                c23 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[9]/label-with-info/span/span[1]").text
                c24 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[10]/field-formatter/span").text
                c23 = c23.replace(" ", "_")
                c23 = c23 + "_Date"
                vars()[c23] = c24

                for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees', 'Stock','Valuation_at_IPO',
                          'Money_Raised_at_IPO', 'IPO_Share_Price', 'IPO_Date'):
                    MyDicts[i] = locals()[i]

            else:
                c21 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[7]/label-with-info/span/span[1]").text
                c22 = driver.find_element_by_xpath("//*[@id='section-ipo-stock-price']/mat-card/div[2]/fields-card/div/span[8]/field-formatter/span").text
                c21 = 'IPO_' + c21
                vars()[c21] = c22

                for i in ('Categories', 'Regions', 'Date', 'Founders', 'Operating_Status', 'Funding_Status', 'Employees', 'Stock','Valuation_at_IPO',
                          'Money_Raised_at_IPO', 'IPO_Date'):
                    MyDicts[i] = locals()[i]

        outputFile = open(Dic[company_num], "w")
        outputFile.write(str(MyDicts))
        outputFile.flush()
        outputFile.close()

    company_num += 1
    time.sleep(2)

