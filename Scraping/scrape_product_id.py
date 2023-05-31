import sys
import time
import json
import selenium
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


capabilities = DesiredCapabilities.EDGE
capabilities['ms:loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Edge(capabilities=capabilities)
# driver.set_page_load_timeout(10)

df_sub_categories = pd.read_csv('data_sub_category.csv')
df_sub_categories = df_sub_categories[133:]
df_products = pd.DataFrame({'product_id': [], 'image': [], 'name': [], 'shop_name': [], 'shopid': [], 'main_category': [], 'sub_category': []})

for index, sub in df_sub_categories.iterrows():

    sub_pages = -1

    for page in range(9):
        print(f"{sub['main_category']} - {sub['sub_category']} / Page {page+1}")

        driver.get(f"{sub['sub_category_link']}?page={page}")

        time.sleep(1)

        if sub_pages == -1:
            sub_pages = int(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopee-mini-page-controller__total'))).text)
        else:
            if (page + 1) > sub_pages:
                break

        logs = driver.get_log("performance")

        for log in logs:
            log = json.loads(log["message"])["message"]

            if ("Network.responseReceived" in log["method"] and "params" in log.keys()):

                if "response" in log["params"].keys():
                    if 'https://shopee.co.id/api/v4/recommend/recommend?bundle=category_landing_page' in (log["params"]["response"]["url"]):

                        try:
                            body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
                            json_data = json.loads(body['body'])

                            for item in json_data['data']['sections'][0]['data']['item']:
                                if item['is_adult'] != True:
                                    for img in item['images']:
                                        df_new = pd.DataFrame({'product_id': [item['itemid']], 'image': [img], 'name': [item['name']], 'shop_name': [item['shop_name']], 'shopid': [item['shopid']], 'main_category': [sub['main_category']], 'sub_category': [sub['sub_category']]})
                                        df_products = pd.concat([df_products, df_new])
                        except:
                            continue

        df_products.to_csv('data_products_id.csv', index=False)


# print(responses)
