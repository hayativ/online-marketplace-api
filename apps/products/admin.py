from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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
