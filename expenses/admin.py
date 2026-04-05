from django.contrib import admin
from .models import Expense
from .models import Budget

admin.site.register(Budget)
# Register your models here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'category', 'date', 'created_at')
    list_filter = ('category', 'date')
    search_fields = ('category', 'description')
    ordering = ('-date',)