from django.shortcuts import render
import time

from .methods import *
from .constants import *

def home_view(request):
    return render(request, 'home.html')

def rec_view(request, **kwargs):
    # term = kwargs.get('term').upper() # for when front end can send to us
    # keywords = OPTIONS.get(term)

    keywords = OPTIONS.get('LOVE')

    tweets = approved_tweets(keywords)

    # will return tweet info consisting of twitter user,
    # profile photo, date of tweet and tweet text
    context = {
        'tweets': tweets,
    }

    return render(request, 'rec.html', context)
