import requests
from bs4 import BeautifulSoup
import time

top = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
with open('douban_top250.csv','a',encoding='utf-8-sig') as f:
    f.write("电影名,评分,排名\n")
    for start_num in range(0,250,25):
        url = f"https://movie.douban.com/top250?start={start_num}"
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text,'html.parser')

        items = soup.find_all('div', class_='item')
        

        for item in items:
            title = item.find('span', class_ = 'title').string
            rating = item.find('span', class_ = 'rating_num').string
        
            if '/' not in title:
                print(f'正在提取{top}')
                f.write(f"电影：{title},评分：{rating},排名：{top}\n")
            top += 1
    time.sleep(0.5)