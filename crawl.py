from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="./chom/chromedriver")
driver.get("https://s.cafef.vn/Lich-su-giao-dich-LDG-1.chn")

file_object = open('sample.txt', 'a')

i = range(100)
for x in i:
    listPost = driver.find_elements(
        By.XPATH, '//*[@id="GirdTable2"]/tbody/tr')
    del listPost[0]
    del listPost[1]
    for row in listPost:
        print(row.text)
        file_object.write(row.text+'\n')
    btnList = driver.find_elements(
        By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ctl03_divHO"]/div/div/table/tbody/tr/td')
    btnList[-1].click()
    sleep(1)

driver.quit()
