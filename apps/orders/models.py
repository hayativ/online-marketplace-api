"""Models to work with user's carts and orders."""
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models import CheckConstraint, Q
from django.core.validators import MaxValueValidator, MinValueValidator


REQUIRES_DELIVERY_CHOICES = [
    ('required', 'Courier delivery required'),
    ('not_required', 'Pickup'),
]


STATUS_CHOICES = [
    ('P', 'Processing'),
    ('S', 'Shipped'),
    ('D', 'Delivered'),
]


class CartItemQuerySet(models.QuerySet):
    """Cart Item QuerySet."""

    def cart_total_price(self):
        """Get total price of user's cart items."""
        if self:
            return sum(cart_item.get_products_price() for cart_item in self)
        return 0

    def cart_total_quantity(self):
        """Get total quantity of items in the user's cart."""
        if self:
            return sum(cart_item.quantity for cart_item in self)
        return 0


class CartItem(models.Model):
    """Model, containing information about a single product in a cart."""
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    # product = models.ForeignKey(
    #     to="Product",
    #     on_delete=models.CASCADE,
    # )
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartItemQuerySet().as_manager()

    class Meta:
        """Meta class."""

        ordering = ("-created_at",)

    def __str__(self):
        """Magic method."""
        return f"{self.user.last_name} {self.user.first_name}'s cart"

    def get_products_price(self):
        """Get the subtotal of a cart."""
        return round(self.product.price * self.quantity, 2)


class Order(models.Model):
    """Order's model."""

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: "
                "'+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    delivery_city = models.CharField(max_length=64)
    delivery_pickup_point = models.CharField(max_length=512)
    delivey_personal_address = models.CharField(
        max_length=512,
        null=True,
        blank=True
    )
    requires_couriers_delivery = models.CharField(
        max_length=32,
        choices=REQUIRES_DELIVERY_CHOICES,
        default='not_required',
    )
    is_paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='P'
    )

    class Meta:
        """Meta class."""

        ordering = ("-created_at",)
        # In case user chose a courier delivery, but did not provide an address
        constraints = [
            CheckConstraint(
                check=(
                    Q(requires_couriers_delivery='not_required') |
                    Q(
                        delivey_personal_address__isnull=False,
                        delivey_personal_address=""
                    )
                ),
                name="requires_delivery_adress_is_not_null"
            )
        ]

    def __str__(self):
        """Magic str method."""
        return (f"Order № {self.pk}"
                f" User: {self.user.first_name} {self.user.last_name}")


class OrderItem(models.Model):
    """Order Item's model."""

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
    # product = models.ForeignKey(
    #     to="Product",
    #     on_delete=models.CASCADE,
    # )
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        ordering = ("-created_at",)

    def __str__(self):
        """Magic str method."""
        return f'Order Item from order: {self.order.id}'


class Review(models.Model):
    """Review model."""

    # product = models.ForeignKey(
    #     to="Product",
    #     on_delete=models.CASCADE,
    # )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_DEFAULT,
        default="Deleted Accounts"
    )
    rate = models.IntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(5)),
        verbose_name='Rating',
        default=0,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        default_related_name = 'reviews'
        ordering = ('-created_at',)

    def __str__(self):
        """Magic str method."""
        return f'Comment from author {self.author.username}'
