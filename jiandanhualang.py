
#coding=utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import urlretrieve

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1515137765; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1515137765',
    'Host':'jandan.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}

url='http://jandan.net/drawings'
print requests.get(url,headers=headers).status_code
html_text=requests.get(url,headers=headers).text
soup=BeautifulSoup(html_text,'html.parser')

headers['Host']='img.jandan.net'

def download_img(img_url):
    print('Downloading %s' %img_url)
    #print img_url.split('/')[-1]
    print(requests.get(img_url,headers=headers).status_code)
    img_content=requests.get(img_url,headers=headers).content
    #img = requests.get(img_url)
    file_name=img_url.split('/')[-1]
    file_path='img/%s' %file_name
    print(file_path)
    with open(file_path,'wb') as img_file:
        img_file.write(img_content)
    #img_file.close()
    #urlretrieve(img_url,'img/%s' %file_name)

for h3 in soup.find_all('div','text'):
    img_url=h3.find('img')['src']
    print img_url
    if 'http' not in img_url:
        img_url='http:'+ img_url
    if not (img_url.endswith('.jpg') or img_url.endswith('.gif')):
        img_url = img_url.replace(img_url.split('.jpg')[1],'')
    download_img(img_url)


# url='http://jandan.net/drawings'
# browser=webdriver.Chrome()
# browser.get(url)


# for element in browser.find_elements_by_css_selector('div[class="text"]'):
#     #print element.find_element_by_css_selector('img').get_attribute('src')
#     img_url=element.find_element_by_css_selector('img').get_attribute('src')
#     download_img(img_url)

