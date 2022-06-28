
from django.urls import path
from . import views

# API's urlpatterns
urlpatterns = [
    path('productapi/', views.ProductApi.as_view(), name='productapi'),
    path('productapi/<int:pk>/', views.ProductApi.as_view(), name='productapi'),
]