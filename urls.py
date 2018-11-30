from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tredegars-home'),
    path('products/', views.products, name='tredegars-products'),
    path('about/', views.about, name='tredegars-about'),
    path('contact/', views.contact, name='tredegars-contact'),
    path('register/', views.register, name='tredegars-register'),
    path('login/', views.login, name='tredegars-login'),
]