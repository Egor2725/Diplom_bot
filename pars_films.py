import requests
from bs4 import BeautifulSoup

def get_html():
    url = "https://afisha.tut.by/film/"
    r = requests.get(url)
    return r.text

def get_films():
    soup = BeautifulSoup(get_html(), 'html.parser')
    list_films = soup.find('div', id='events-block').find_all('ul')
    films_name = []
    films_href = []
    for f in list_films:
        for article in f.find_all('a', {'class': 'name'}):
            films_name.append(article.text)
    for f in list_films:
        for article in f.find_all('a', {'class': 'media'}, href=True):     
            films_href.append(article['href'])
            # print(article['href'])

    # for f in list_films:
    #     for article in f:
    #         li = atricle.find_all('li', {'class': 'lists__li '}):
    #             for li in article:
    #                 h = li.find('a', {'class': 'name'})['href']
            
    films_list = dict(zip(films_name, films_href))    
    return films_list
#     print(films_list)




