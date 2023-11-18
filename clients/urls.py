from django.urls import path
from clients import views
from clients.views import AditionalDataView

urlpatterns = [
    path('aditionalData/', views.AditionalDataView.as_view(), name='aditionalData'),
    path('registerOrder/', views.RegisterOrderView.as_view(), name='registerOrder'),
    path('orderDetail/', views.OrderDetailView.as_view(), name='orderDetail'),
]
