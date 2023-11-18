from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
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
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, primary_key=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} - Product {self.product_id}"
    
class Children(models.Model):
    children_id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    genre = models.CharField(max_length=50)
    study = models.BooleanField(default=False)
    play_videogames = models.BooleanField(default=False)
    videogames_platform = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class BirthPlace(models.Model):
    birth_id =  models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Lugar de Nacimiento - {self.ciudad}, {self.departamento_estado}, {self.pais}"

class PlaceLocation(models.Model):
    place_id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Ubicación - {self.ciudad}, {self.departamento_region_estado}, {self.pais}"

class CivilStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_type = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"Ubicación - {self.ciudad}, {self.departamento_region_estado}, {self.pais}"

class CustomerAditionalData(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    children = models.ManyToManyField(Children, blank=True)
    birth_place = models.ManyToManyField(BirthPlace, blank=True)
    place_location = models.ManyToManyField(PlaceLocation, blank=True)
    hobbies = models.TextField(blank=True)
    sports = models.TextField(blank=True)
    civil_status = models.CharField(max_length=50, blank=True)
    interest_categories = models.ManyToManyField(CategoryProducts, blank=True)

    def __str__(self):
        return f"{self.customer.email} - Datos Adicionales"


