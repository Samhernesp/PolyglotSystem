from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Customer', default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    home_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class CategoryProducts(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.description

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_code = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

class Orders(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    shipped_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.order_number} by {self.customer_id}"

class OrderDetail(models.Model):
    order_number = models.ForeignKey(Orders, on_delete=models.CASCADE, primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} - Product {self.product_id}"