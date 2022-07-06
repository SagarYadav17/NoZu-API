from rest_framework import serializers
from expenseTracker.models import Expense, Category


class CategorySerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Expense
        fields = "__all__"
