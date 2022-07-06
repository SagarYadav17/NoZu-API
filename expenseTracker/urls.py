from django.urls import path
from expenseTracker import views

urlpatterns = [
    path("category/", views.ExpenseCategoryView.as_view(), name="expense-expense-category"),
    path("expense/", views.ExpenseView.as_view(), name="expense-expense-list-create"),
    path("expense/<int:id>/", views.ExpenseDetailView.as_view(), name="expense-expense-detail"),
]
