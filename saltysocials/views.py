from django.shortcuts import render
import time

from .methods import *
from .constants import *

def home_view(request):
    return render(request, 'home.html')

def rec_view(request, **kwargs):
    # term = kwargs.get('term').upper() # for when front end can send to us
    # keywords = OPTIONS.get(term)

    # approved_tweets = approved_tweets(keywords)


    keywords = OPTIONS.get('LOVE')
    approved_tweets = [['id', 'hello this is a tweet', 'mar 5 2022']]

    # will return tweet info consisting of twitter user,
    # profile photo, date of tweet and tweet text
    context = {
        'tweets': approved_tweets,
    }

    return render(request, 'rec.html', context)