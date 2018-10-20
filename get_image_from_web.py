import requests
import bs4
import re

def open_url(url):
    request = requests.get(url).content
    return bs4.BeautifulSoup(request,features="html5lib")    
def get_image_url(data, i):
    img = str(data.select('.tri_img_wrap .tri_img_one .tri_img'))
    img = re.findall(r'src="[\S]+', img)[i] #изменяя [n] Получаем разные картинки
    img = re.findall(r'"\S+"', img)[0].replace('"', "")
    print(img)
    return img
def save_image(url, i):
    path = '{}.jpg'.format(i)
    img = requests.get(url)
    with open(path, 'wb') as file:
        file.write(img.content)    
def main():
    tag=input('Введите тему картинки на английском-->')
    url='https://picjumbo.com/?s={}'.format(tag)
    while True:
        try:
            kol = int(input('Количество картинок->>'))
            break;
        except ValueError:
            print('Введите цифру!')
    for i in range(1, kol+1):
        save_image(get_image_url(open_url(url), i), i)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit
    except IndexError:
        print("Слишком много картинок=)")
        exit
    except requests.exceptions.MissingSchema:
        print('По запросу ничего не найдено=(')
