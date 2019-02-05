from bs4 import BeautifulSoup as bs
import requests
import re
import os
import csv

path = '/Users/us579/Desktop/douban/'


header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url_list = ['https://movie.douban.com/top250']
url_list+=['https://movie.douban.com/top250?start=%d&filter=' % page for page in range(0,250,25)]



def pic_download(path,url,name):
        r = requests.get(url)
        with open(path+name,'wb') as f:
                f.write(r.content)


def mov_list(url):
        response = requests.get(url,header)
        response.encoding = 'utf-8'
        html = bs(response.text,'html.parser')
        data = html.find('ol',{'class':'grid_view'})
        lis = data.find_all('li')
        movies = []
        for num in lis:
                rank = num.find('em').get_text()
                name = num.find('img')['alt']
                pic = num.find('img')['src']
                #print(name)
                inf = num.find('p').get_text()
                #print(inf)
                director = re.findall('导演:\s(.*?)\s',inf)[0]
                #print(director)
                actor = re.findall('主演:\s(.*?)\s',inf)
                #print(actor)
                if len(actor) == 0 :
                        actor = '匿名'
                else:
                        actor = actor[0]
                year = re.search(r'\d{4}',inf).group()
                district = re.findall('\s/\s(.*?)\s/\s',inf)
                #print(year)
                #print(district)
                if len(district) > 1:
                        area = district[1]
                else:
                        area = district[0]
                score = num.select('span.rating_num')[0].get_text()
                summary = num.select('span.inq')
                #print(pic)
                if len(summary) > 1:
                        summary = ''
                elif not summary:
                        summary = ''
                else:
                        summary = summary[0].get_text()

                try:
                        if not os.path.exists(path):
                                os.mkdir(path)
                        file_name = '{}.png'.format(name)
                except IOError as e:
                        print("IOError")

                pic_download(path,pic,file_name)

                sets = (rank,name,director,actor,year,area,score,summary)
                movies.append(sets)
        return movies



def save():
        headers = ['排名', '名字', '导演', '主演', '年份', '地区', '评分', '简介']
        with open('top250.csv',encoding='UTF-8',mode='w') as f:
                file = csv.writer(f)
                file.writerow(headers)
                for url in url_list:
                        details = mov_list(url)
                        for i in details:
                                file.writerow(i)


if __name__ == '__main__':
        save()

