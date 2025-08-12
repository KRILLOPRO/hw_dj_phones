from django.urls import path, include
from phones import views

urlpatterns = [
    path('', views.show_catalog, name='home'),
    path('catalog/', views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.show_product, name='product'),
]