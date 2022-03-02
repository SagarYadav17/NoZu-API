from rest_framework import serializers

from expenseTracker.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def create(self, validated_data):
        expense = Expense.objects.create(**validated_data)
        return expense
