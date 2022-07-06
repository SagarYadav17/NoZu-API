from django.urls import path, include
from rest_framework.routers import DefaultRouter

from expenseTracker.views import ExpenseView, CategoryView

app_name = "expense"

router = DefaultRouter()
router.register("expense", ExpenseView, basename="expense-category")
router.register("category", CategoryView, basename="expense-expense")

urlpatterns = [
    path("", include(router.urls)),
]
