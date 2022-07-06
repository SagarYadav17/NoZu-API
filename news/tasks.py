import threading
import requests

from config.config import BASE_NEWS_URL, CATEGORIES, COUNTRIES
from news.utils import create_article


class FetchNewsTread(threading.Thread):
    def run(self):
        for country in COUNTRIES:
            # Top News
            url = f"{BASE_NEWS_URL}&country={country}"

            response = requests.get(url).json()

            for article in response.get("articles"):
                create_article(article, country, "top")

            # Category Based News
            for category_name in CATEGORIES:
                url = f"{BASE_NEWS_URL}&country={country}&category={category_name}"

                response = requests.get(url).json()

                for article in response.get("articles"):
                    create_article(article, country, category_name)
