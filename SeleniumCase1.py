#取得網頁標籤

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH="C:/Users/Jackie/Desktop/Python/chromedriver.exe"
driver=webdriver.Chrome(PATH)
#去哪個網址
driver.get('https://www.dcard.tw/f')
search=driver.find_element(By.TAG_NAME,'input')
#輸入內容
search.send_keys('比特幣')
#按下Enter
search.send_keys(Keys.RETURN)
#頁面跳轉後要停一下,網頁資料才會更新
time.sleep(3)

titles=driver.find_elements(By.CSS_SELECTOR,"a[class='sc-417133b6-3 jNOCIa']")
for title in titles:
    print(title.text)

#time.sleep(5)
#driver.quit()