from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:pk>/', views.getSoloProducto),
    path('get/', views.getProducto),
    path('post/', views.postProducto),
    path('put/<int:pk>/', views.putProducto),
    path('delete/<int:pk>/', views.deleteProducto),
]   



