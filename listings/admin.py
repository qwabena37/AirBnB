from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price_per_night", "available", "created_at")
    list_filter = ("city", "available")
    search_fields = ("title", "city", "description")

