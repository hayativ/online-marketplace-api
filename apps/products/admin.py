# Django modules
from django.contrib import admin

# Project modules
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin configuration class.
    """

    list_display = (
        "id",
        "name",
        "description",
    )
    search_fields = ("name",)
    list_filter = (
        "name",
    )
    fieldsets = [
        (
            "Category Information",
            {
                "fields": (
                    "name",
                    "description",
                ),
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin configuration class.
    """

    list_display = (
        "id",
        "name",
        "category",
        "seller",
        "price",
        "created_at",
    )
    search_fields = (
        "name",
        "category__name",
        "seller__email",
    )
    list_filter = (
        "category",
        "seller",
        "created_at",
    )
    ordering = ("-created_at",)

    fieldsets = [
        (
            "Product Information",
            {
                "fields": (
                    "name",
                    "description",
                    "price",
                    "image",
                ),
            },
        ),
        (
            "Relations",
            {
                "fields": (
                    "category",
                    "seller",
                ),
            },
        ),
        (
            "Date Information",
            {
                "fields": ("created_at",),
            },
        ),
    ]

    readonly_fields = ("created_at",)
