#Youtube影片網址:https://www.youtube.com/watch?v=ximjGyZ93YQ
#要先下載ChromeDriver;版本要與目前使用的Chrome版本相同

from selenium import webdriver

PATH="C:/Users/Jackie/Desktop/Python/chromedriver.exe"
driver=webdriver.Chrome(PATH)
#去哪個網址
driver.get('https://www.chinatimes.com/?chdtv')
print(driver.title)
driver.quit()