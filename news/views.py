# REST FRAMEWORK
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

# Cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Models & Serializers
from news.models import Article

from news.serializers import ArticlesListSerializer

# Others
from datetime import date, timedelta
from news.tasks import FetchNewsTread


class FetchNews(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        FetchNewsTread().start()
        return Response({"status": True})


class DeleteOldNews(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        old_news = Article.objects.filter().exclude(publishedAt__date__gte=(date.today() - timedelta(days=3)))
        old_news.delete()

        return Response({"status": f"{old_news.count()} news are deleted!"})


class NewsView(ListAPIView):
    serializer_class = ArticlesListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("title",)

    def get_queryset(self):
        queryset = Article.objects.filter().order_by("-publishedAt")

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__name=category)

        return queryset

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
