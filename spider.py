# -*- coding: UTF-8 -*-

import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook





DOWNLOAD_URL = 'http://movie.douban.com/top250'
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def parse_html(html):

    soup = BeautifulSoup(html)

    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

    for movie_li in movie_list_soup.find_all('li'):

        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()

        print(movie_name)

if __name__ == '__main__':
    content = download_page(DOWNLOAD_URL)
    parse_html(content)