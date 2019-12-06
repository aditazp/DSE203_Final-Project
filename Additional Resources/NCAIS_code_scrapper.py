import time
import csv
from selenium import webdriver
import pickle
import pandas as pd
from selenium.webdriver.common.keys import Keys


page_url = "https://siccode.com/"


driver = webdriver.Chrome('/Users/erikhoye/Desktop/Data_Integration_Final_Project/wikepedia_webscrapper/wikepedia_webscrapper/chromedriver')

company_list = ['Cisco Systems', 'VMware', 'Big Switch Networks', 'Extreme Networks', 'Arista Networks',
                'Hewlett Packard Enterprise', 'Juniper Networks', 'Huawei', 'Netgear','Allied Telesis',
                 'Lenovo', 'NEC', 'Mellanox Technologies']

annoying = ['https://siccode.com/business/d-link-systems-inc']

# creating edge properties table for Neo4j insertion
company_codes = pd.DataFrame(columns=['Company', 'Code'])

t = {'Company': ['Cumulus Networks', 'Dell EMC', 'ZTE'], 'Code': [511518, 511210, 511210]}
temp = pd.DataFrame(data=t)
company_codes = company_codes.append(temp, ignore_index=True)

for company in company_list:
    driver.get(page_url)
    searchBox = driver.find_element_by_id("keyword_m")
    searchBox.send_keys(company)
    driver.find_element_by_xpath("/html/body/div[1]/article/section[1]/div/form/div/div[2]/input").click()
    temp = driver.find_element_by_xpath("//*[@id='result-top-companies']/ul/li[1]/a/div[1]").text
    driver.find_element_by_xpath("//*[@id='result-top-companies']/ul/li[1]/a/div[1]").click()
    companyCode = driver.find_element_by_xpath("//*[@id='description']/div[2]/div/div/a[2]").text

    t = {'Company': [company], 'Code': [int(companyCode[11:17])]}
    temp = pd.DataFrame(data=t)
    company_codes = company_codes.append(temp, ignore_index=True)
    time.sleep(2)

for company in annoying:
    page_url = company
    driver.get(page_url)
    companyCode = driver.find_element_by_xpath("//*[@id='description']/div[2]/div/div/a[2]").text

    t = {'Company': ['D-Link'], 'Code': [int(companyCode[11:17])]}
    temp = pd.DataFrame(data=t)
    company_codes = company_codes.append(temp, ignore_index=True)

company_codes.to_pickle("company_codes.pkl")