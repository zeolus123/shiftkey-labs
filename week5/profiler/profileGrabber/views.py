from django.shortcuts import render, get_object_or_404
from .models import SavedUser, SavedTweet
from .forms import *
from . import tweet_profiler

def index(request):
    context = {}
    return render(request, 'profileGrabber/index.html', context)

def discover(request):
    profile = tweet_profiler.get_profile("cd_conrad")
    influencer = "NO"

    if request.method == 'POST':
        render_handle = HandleForm(request.POST)
        render_push = PushForm(request.POST)
        if render_handle.is_valid():
            profile = tweet_profiler.get_profile(render_handle.cleaned_data['twitter_handle'])
            render_push = PushForm()
        elif render_push.is_valid():
            profile = tweet_profiler.get_profile(render_push.cleaned_data['push_handle'])

            try:
                saved_tweets = tweet_profiler.get_tweets()
                #saving the new users
                s = SavedUser(
                    source = render_push.cleaned_data['push_source'],
                    handle = profile.screen_name,
                    name = profile.screen_name,
                    followers = profile.followers_count,
                    following = profile.friends_count,
                    location = profile.location,
                    influencer = influencer,
                    description= profile.description,
                )
                s.save()
            except:
                s = ""

            #Trying to save the tweets
            try:
                saved_tweets = tweet_profiler.get_tweets(profile.screen_name)
                for tweet in saved_tweets:
                    t = SavedTweet(
                        id_str= tweet.id_str,
                        text= tweet.text,
                        created_at= tweet.created_at,
                        owner= profile.screen_name
                    )
                    t.save()
            except:
                t = ""
            render_handle = HandleForm()
        else:
            render_handle = HandleForm()
            render_push = PushForm()

    if profile.followers_count > 500:
        influencer = "YES"
    context = {
        'profile': profile,
        'influencer': influencer,
    }

    return render(request, 'profileGrabber/discover.html', context)


def collection(request):
    saved_tweets = SavedTweet.objects.all()

    context = {
        'saved_tweets': saved_tweets,
    }

    return render(request, 'profileGrabber/collection.html', context)
