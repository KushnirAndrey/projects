import requests
import bs4
import re

tag=input('Введите тему картинки на английском-->')
kol = int(input('Количество картинок->>'))#исключить буквы
url='''https://www.dreamstime.com/search.php?securitycheck=e0f88b4e731696aec73a2b17b6ccd2f5&
    firstvalue={}&lastsearchvalue=&srh_field={}&s_ph=y&s_il=y&s_video=y&s_audio=y'''.format(tag,tag)
#https://picjumbo.com/one-little-angry-cat/ получать картинки с этого сайта
url = 'https://picjumbo.com/?s={}'.format(tag)
def open_url(url):
    request = requests.get(url).content
    return bs4.BeautifulSoup(request,features="html5lib")    
def get_image_url(data, i):
    img = data.findAll('img')
    image_url = img[i]
    return image_url['src'].replace('/t/', '/z/')
def save_image(url, i):
    path = '{}.jpg'.format(i)
    img = requests.get(url)
    with open(path, 'wb') as file:
        file.write(img.content)    
def main():
    for i in range(kol):
        save_image(get_image_url(open_url(url), i), i)

if __name__ == '__main__':
    main()

