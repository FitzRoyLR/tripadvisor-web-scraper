# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:46:14 2020

@author: Louis Régis
"""

import sys
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# default path to file to store data
path_to_file = "C:/Users/Louis Régis/Documents/Ontario attractions.csv"
# default number of scraped pages
num_page = 100

# default tripadvisor website of hotel or things to do (attraction/monument) 
url = "https://www.tripadvisor.com/Attractions-g154979-Activities-a_allAttractions.true-Ontario.html"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)


# change the value inside the range to save more or less reviews
for i in range(0, num_page):

    time.sleep(1)

    container = driver.find_elements_by_xpath("//div[@class='_25PvF8uO _2X44Y8hm']")
    

    for j in range(len(container)):

        try: 
            
            interest = container[j].find_element_by_xpath(".//span[contains(@class, '_21qUqkJx')]").text
            title = container[j].find_element_by_xpath(".//a[contains(@class, '_1QKQOve4')]").text
            page_link = container[j].find_element_by_xpath(".//a[contains(@class, '_1QKQOve4')]").get_attribute("href")
            reviews = container[j].find_element_by_xpath("//div/span[contains(@class, 'HLvj7Lh5 _1L-8ZIjh _2s3pPhGm')]/span").text
            photo = container[j].find_element_by_xpath(".//source")
            photo_src = photo.get_attribute("srcset").split(" ")[0]
            
    
        except: 
            pass
        
        csvWriter.writerow([title, photo_src, page_link, interest]) 
        
    # change the page       
    try: 
        driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()
    except: 
        pass


driver.quit()