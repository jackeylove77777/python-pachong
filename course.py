import time
import requests as req
from openpyxl import Workbook

header = {
  'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"
}

wb = Workbook()
ws = wb.active

nav = ['标题','价格','作者']
ws.append(nav)

for index in range(36):
  time.sleep(1)
  url = 'https://api.hahow.in/api/courses?limit=24&page='
  url = url+str(index)
  print(url)
  res = req.get(url,header)
  print(res.status_code)
  json = res.json()
  for data in json['data']:
    row = []
    row.append(data['title'])
    row.append(data['price'])
    row.append(data['owner']['username'])
    print(row)
    ws.append(row)

wb.save('course.xlsx')