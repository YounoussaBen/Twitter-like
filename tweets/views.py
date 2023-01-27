from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweets
# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    
    
    data = {
        "id": tweet_id,

    }
    status = 200
    try:
        obj = Tweets.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)

    # return HttpResponse(f"<h1>hello {tweet_id} - {obj.content} </h1>")