from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Models & Serializers
from expenseTracker.models import Expense, Category
from expenseTracker.serializers import ExpenseSerializer

# Cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ExpenseCategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    # Cache page for the requested url
    @method_decorator(cache_page(60 * 15))
    def get(self, request):
        queryset = Category.objects.all()
        return Response(queryset.values("id", "name"))


class ExpenseView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset


class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExpenseSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset
