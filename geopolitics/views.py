from django.shortcuts import render
from .services.newsapi_service import NewsAPIService

def geopolitical_news(request):
    service = NewsAPIService()

    query = request.GET.get("q", "geopolitics OR war OR diplomacy")
    data = service.everything(query=query)

    return render(
        request,
        "geopolitics/news.html",
        {"articles": data.get("articles", [])},
    )