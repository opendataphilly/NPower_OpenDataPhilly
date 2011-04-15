from datetime import datetime
from django.conf import settings
from django.core.cache import cache
from models import TwitterCache
import twitter
import simplejson as json

def latest_tweets( request ):
    tweets = cache.get( 'tweets' )

    if tweets:
        return {"tweets": tweets}
    
    tweets = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[:3]
    if tweets.count < 3:
        tweet_cache = []
        for t in TwitterCache.objects.all():
            tc = json.JSONDecoder().decode(t.text)
            tc['date'] = datetime.strptime( tc['created_at'], "%a %b %d %H:%M:%S +0000 %Y" )
            tweet_cache.append(tc)
        return {'tweets': tweet_cache}
        
    TwitterCache.objects.all().delete()
    for tweet in tweets:
        tweet.date = datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
        t = TwitterCache(text=tweet.AsJsonString())
        print t.text
        t.save()
    cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )
    
    return {"tweets": tweets}

def get_current_path(request):
    return {'current_path': request.get_full_path()}