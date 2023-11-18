from django.contrib import admin
from .models import Customer,Products,Orders,OrderDetail,CategoryProducts,CustomerAditionalData

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(CategoryProducts)
admin.site.register(CustomerAditionalData)