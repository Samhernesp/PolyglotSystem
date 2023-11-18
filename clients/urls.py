from django.urls import path
from clients import views
from clients.views import AditionalDataView

urlpatterns = [
      path('aditionalData/', views.AditionalDataView.as_view(), name='aditionalData'),
]
