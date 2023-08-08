import requests
from bs4 import BeautifulSoup
import os
import sys




class OKMFetch(object):
    def __init__(self, url) -> None:
        self.url = url
        # # 从URL下载HTML页面
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')

        # # 使用选择器选择页面的标题，并作为文件名
        # title = soup.title.string.replace('\n', '').strip().replace(' ', '_')
        # self.filename = title + '.html'

        # # 将HTML页面保存到本地
        # with open(self.filename, 'w', encoding='utf-8') as file:
        #     file.write(response.text)

    def parse_arxiv(self, html_data):
        pass

    def parse_gmu_edu(self, html_data):
        doi_link = html_data.find('section', class_='item doi').find('a')['href']
        return doi_link

    def parse_arxiv(self, html_data):
        pass

    def parse_arxiv(self, html_data):
        pass

    def run(self):
        self.filename = "Overview_of_research_on_large_language_model_privacy_-_Open_Knowledge_Maps.html"

        # 重新使用BeautifulSoup解析本地文件
        with open(self.filename, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # 用一个selector选择页面中的一个列表
        list_selector = '#papers_list'  # 替换为正确的选择器
        item_list = soup.select_one(list_selector)

        # 用另外两个selector分别选择列表中的标题和URL链接
        title_selector = '#paper_list_title' # 替换为正确的选择器
        url_selector = '#list_holder > div > div.list_metadata > div.doi_outlink > span > a'     # 替换为正确的选择器

        # 创建字典保存标题和链接
        result_dict = {}
        for title_tag, url_tag in zip(item_list.select(title_selector), item_list.select(url_selector)):
            result_dict[title_tag.text.strip()] = url_tag['href']

        # 打印字典
        print(result_dict)


# 指定URL
url = 'https://openknowledgemaps.org/map/282a4733a18a9e0b030cb4adbbf6dae1'
if len(sys.argv) > 1:
    url = sys.argv[1]
    
okm_fetch = OKMFetch(url)
okm_fetch.run()
