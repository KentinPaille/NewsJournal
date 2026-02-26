from newsapi import NewsApiClient
from django.conf import settings

class NewsAPIService:
    def __init__(self):
        self.client = NewsApiClient(api_key=settings.NEWSAPI_KEY)

    def everything(self, query, language="en", from_date=None, to_date=None):
        return self.client.get_everything(
            q=query,
            language=language,
            from_param=from_date,
            to=to_date,
            sort_by="relevancy",
        )