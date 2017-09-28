from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup


def imbdparser(request):
    # url of current Week premiere
    url = 'http://www.imdb.com/movies-in-theaters/'

    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    # Get HTML block with film list and parse it
    movie_containers = html_soup.find_all('div', class_='list_item')
    # Create list of  all movies for fill it later
    movie_list = []
    # ===========Test part============
    #first_movie = movie_containers[0]
    # stars_li = '|'.join(map(str, [stars.text for stars in first_movie.select('span[itemprop="name"]')]))
    # print(stars_li)
    # Get list of all films on parsed page
    # f = first_movie.find('span', class_='metascore favorable')
    # print(f)
    # ========== End test ===========
    for movie in movie_containers:
        # Check rating. Because Without check get an error NoneType object have not text attr
        rating = movie.find('span', class_='metascore favorable')
        if rating is not None:
            rating = rating.text
        else:
            rating = '*'
        movie_list.append({
            'title':movie.h4.a['title'],
            'description':movie.find('div', class_='outline').string,
            'image': movie.img['src'],
            'director': movie.h5.find_next('a').text,
            # Get stars list and clear from tags and \n, convert list to string
            'stars': ','.join(map(str, [stars.text.strip('\n') for stars in movie.select('span[itemprop="actors"] > span')])),
            # get rating
            'rating': rating,
            # Get rating list, clear from tags and \n, convert list to string
            'genre': '|'.join(map(str, [genre.text.strip('\n') for genre in movie.select('span[itemprop="genre"]')])),

          }
        )

    return render(request, 'imbd/index.html', {'movie_list':movie_list})
