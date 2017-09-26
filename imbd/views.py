from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup


def imbdparser(request):
    url = 'http://www.imdb.com/movies-in-theaters/'

    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    print(type(html_soup))

    return render(request, 'imbd/index.html', {'response':response})

# Create your views here.
