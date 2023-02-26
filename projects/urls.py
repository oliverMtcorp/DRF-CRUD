from django.urls import include, path 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView 
from django.urls import path
from . import views  

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name="api:schema"), name='swagger'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'),
    path('get/<int:pk>/', views.getSoloProducto),
    path('get/', views.getProducto),
    path('post/', views.postProducto),
    path('put/<int:pk>/', views.putProducto),
    path('delete/<int:pk>/', views.deleteProducto),
]




