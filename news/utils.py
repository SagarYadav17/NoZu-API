from news.models import Source, Country, Category, Article


def create_article(article, country, category_name):
    source_name = article.get("source").get("name")
    source_obj = Source.objects.get_or_create(name=source_name)[0]
    country_obj = Country.objects.get_or_create(name=country)[0]
    category_obj = Category.objects.get_or_create(name=category_name)[0]

    objs = Article.objects.filter(url=article.get("url"))

    if not objs:
        Article.objects.create(
            source=source_obj,
            category=category_obj,
            country=country_obj,
            title=article.get("title"),
            author=article.get("author"),
            description=article.get("description"),
            url=article.get("url"),
            urlToImage=article.get("urlToImage"),
            publishedAt=article.get("publishedAt"),
        )

    return True
