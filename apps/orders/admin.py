from django.contrib import admin

from .models import Order, OrderItem, CartItem, Review


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
        "quantity",
        "created_at",
    )
    search_fields = ("user__email", "product__name")
    list_filter = ("quantity",)
    fieldsets = [
        (
            "Cart Information",
            {
                "fields": ["user", "product", "quantity"],
            },
        ),
        (
            "Date-Time Information",
            {
                "fields": ["created_at"],
            },
        ),
    ]
    readonly_fields = ("created_at",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "name",
        "price",
        "quantity",
        "created_at",
    )
    search_fields = ("order", "product", "name")
    list_filter = ("quantity", "price")
    fieldsets = [
        (
            "Order Information",
            {
                "fields": ["order"],
            },
        ),
        (
            "Product Information",
            {
                "fields": ["product", "name", "quantity", "price"],
            },
        ),
        (
            "Date-Time Information",
            {
                "fields": ["created_at"],
            },
        ),
    ]
    readonly_fields = ("created_at",)


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone_number",
        "delivery_city",
        "delivery_pickup_point",
        "delivery_personal_address",
        "requires_couriers_delivery",
        "status",
        "created_at"
    )
    search_fields = (
        "user__email",
        "product__name",
        "user__phone",
        "delivery_city",
        "delivery_personal_address",
        "delivery_pickup_point",
        "status",
    )
    list_filter = ("status", "created_at")
    fieldsets = [
        (
            "User Information",
            {
                "fields": ["user", "phone_number"],
            },
        ),
        (
            "Destination Information",
            {
                "fields": [
                    "delivery_city",
                    "delivery_pickup_point",
                    "requires_couriers_delivery",
                ],
            },
        ),
        (
            "Status Information",
            {
                "fields": [
                    "status",
                ],
            },
        ),
        (
            "Date-Time Information",
            {
                "fields": ["created_at"],
            },
        ),
    ]
    readonly_fields = ("created_at",)


@admin.register(Review)
class ReviewItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "product",
        "rate",
        "created_at",
    )
    search_fields = ("author__username", "product__name")
    list_filter = ("rate",)
    fieldsets = [
        (
            "Review Information",
            {
                "fields": ["author", "product", "rate", "text"],
            },
        ),
        (
            "Date-Time Information",
            {
                "fields": ["created_at"],
            },
        ),
    ]
    readonly_fields = ("created_at",)
