
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PATH = 'E:/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get('https://juejin.cn/')
driver.implicitly_wait(10)


input = driver.find_element(By.CLASS_NAME,'search-input')
input.clear()
input.send_keys('React')
input.send_keys(Keys.RETURN)



titles = driver.find_elements(By.CSS_SELECTOR,'.title > .text-highlight')
enter_title = None
if titles!=None:
  for title in titles:
    print(title.text)
    if title.text.find('vue')!=-1:
      enter_title=driver.find_element(By.CSS_SELECTOR,'.title-row > .title')

dialog_close = driver.find_element(By.CLASS_NAME,'icon-close')
dialog_close.click()

if enter_title!=None:
  enter_title.click()
  time.sleep(3)
  driver.close()


time.sleep(10)
driver.quit()


