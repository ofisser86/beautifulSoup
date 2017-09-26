from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup


def imbdparser(request):
    url = 'http://www.imdb.com/movies-in-theaters/'

    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_='list_item')
    movie_list = []
    # first_movie = movie_containers[0]
    # stars_li = first_movie.select('span[itemprop="name"]')
    # for i in stars_li:
    #     print(type(i.text))
    for movie in movie_containers:
        movie_list.append({
            'title':movie.h4.a['title'],
            'description':movie.find('div', class_='outline').text,
            'image': movie.img['src'],
            'director': movie.h5.find_next('a').text

          }
        )
        rating = movie.find('span', class_='metascore mixed')
        if rating is not None:
            movie_list.append({'rating':rating})
        else:
            movie_list.append({'rating': '*'})
        genre_list = movie.select('span[itemprop="genre"]')
        for genre in genre_list:
            movie_list.append({'genre':genre.text})
        # print(movie.select('span[itemprop="genre"]').text)
        stars_list = movie.select('span[itemprop="name"]')
        for star in stars_list:
            movie_list.append({'star': star.text})


    return render(request, 'imbd/index.html', {'movie_list':movie_list})

# Create your views here.
