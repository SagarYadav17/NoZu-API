from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Models & Serializers
from expenseTracker.models import Expense, Category
from expenseTracker.serializers import ExpenseSerializer, CategorySerializers

# Cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Custom
from config.utils import delete_cache


class CategoryView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializers
    http_method_names = ["get", "post", "patch", "delete"]

    cache_key_prefix = "expenseTracker.category"

    def get_queryset(self):
        queryset = Category.objects.filter(user=self.request.user)
        return queryset

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 5, key_prefix=cache_key_prefix))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().partial_update(request, *args, **kwargs)


class ExpenseView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    cache_key_prefix = "expenseTracker.expense"

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 5, key_prefix=cache_key_prefix))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        delete_cache(self.cache_key_prefix)
        return super().partial_update(request, *args, **kwargs)
