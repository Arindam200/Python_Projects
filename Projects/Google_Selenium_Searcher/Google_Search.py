from re import search
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import json
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
outputfile = open('xyz.csv', 'w')
csvwriter = csv.writer(outputfile)
with open('amfoss.json') as f :
    data = json.loads(f.read())
for i in range(len(data)):
    link = []
    time.sleep(2)
    query = data[i]["School_Name_EN"]
    url = f"https://www.google.com/search?q={query}"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    search = soup.find('div', class_="yuRUbf")
    z = search.a.get('href')
    z = str(z)
    link.append(z)
    print(query)
    csvwriter.writerow(link)
