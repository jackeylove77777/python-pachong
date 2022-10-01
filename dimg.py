from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as req
import wget #查不到怎么添加user-agent请求头，所以改成requests
import os
PATH = 'E:/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get('https://pixabay.com/zh/')
driver.implicitly_wait(10)



#创建存放图片的目录
dir = os.path.join('美女')
if os.path.exists(dir):
  os.rmdir(dir)
os.mkdir(dir)

input = driver.find_element(By.XPATH,'//*[@id="hero"]/div[4]/form/div/span/input')
input.clear()
input.send_keys('美女')
input.send_keys(Keys.RETURN)

#等待搜素结果
search = WebDriverWait(driver,10).until(
  EC.presence_of_element_located((By.XPATH,'//*[@id="header_inner"]/div[4]/form/div/span/input'))
)
#滑动
for i in range(3):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

items = driver.find_elements(By.CSS_SELECTOR,'.item > a > img')
print(len(items))


header = {
  'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
}

cnt = 1
for i in items:
  src = i.get_attribute('src')
  print(src)
  if src.endswith('.jpg'):
    save_path = os.path.join(dir,'meinv'+str(cnt)+".jpg")
    img = req.get(src,headers=header).content
    with open(save_path,'wb') as f:
      f.write(img)
    cnt+=1

driver.quit()


