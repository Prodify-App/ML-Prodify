import requests
import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

main_categories = pd.read_csv('data_main_category.csv')

id_main_category = []
main_category = []
id_sub_category = []
sub_category = []
sub_category_link = []

for index, mc in main_categories.iterrows():
    driver.get(mc['link'])
    time.sleep(1)

    try:
        driver.find_element(By.CLASS_NAME, 'shopee-category-list__toggle-btn').click()
    except:
        pass

    data = driver.find_elements(By.CLASS_NAME, 'shopee-category-list__sub-category')

    for d in data:
        name = d.text
        link = d.get_attribute("href")

        id_main_category.append(mc['id_main_category'])
        main_category.append(mc['main_category'])
        id_sub_category.append(link.split('.')[-1])
        sub_category.append(name)
        sub_category_link.append(link)


df = pd.DataFrame({'id_main_category': id_main_category, 'main_category': main_category, 'id_sub_category': id_sub_category, 'sub_category': sub_category, 'sub_category_link': sub_category_link})
df.to_csv('data_sub_category.csv', index=False)

print(df)
