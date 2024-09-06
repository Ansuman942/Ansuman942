from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def index(request):
    all_news =News.objects.all()
    return render(request,"home.html",{"news": all_news,"len": len(all_news)})




def detail_news(request, news_id):
    news = News.objects.get(News, id=news_id)  # Fetch the news item
    return render(request, "news/detail.html", {"news": news})  # Ensure the template path is correct