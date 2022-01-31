from rest_framework import serializers
from blog.models import Post
from django.contrib.humanize.templatetags.humanize import naturalday


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("author", "author_username", "title", "summary", "content", "published_date", "slug")

    def get_author(self, obj):
        return obj.author.get_full_name()

    def get_author_username(self, obj):
        return obj.author.username

    def get_published_date(self, obj):
        return naturalday(obj.published_date)


class PostListSerializer(serializers.ModelSerializer):
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "title", "published_date", "summary", "slug")

    def get_published_date(self, obj):
        return naturalday(obj.published_date)
