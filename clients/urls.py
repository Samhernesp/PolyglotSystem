from django.urls import path
from clients import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landingPage'),
    path('aditionalData/', views.ClientRegistrationView.as_view(), name='aditionalData'),
    path('registerOrder/', views.RegisterOrderView.as_view(), name='registerOrder'),
    path('orderDetail/', views.OrderDetailView.as_view(), name='orderDetail'),
    path('registerCouple/', views.AddCoupleView.as_view(), name='registerCouple'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
