from django.core.cache import cache


def delete_cache(key_prefix):
    keys = cache.keys(f"views.decorators.cache.cache_page.{key_prefix}*")
    if keys and len(keys) == 1:
        cache.delete(keys[0])
        return True

    return False
