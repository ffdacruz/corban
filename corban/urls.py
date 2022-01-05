from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from production.api import viewsets


route = routers.DefaultRouter()
route.register(r'users', viewsets.UserViewSet, basename="Users")
route.register(r'promoters', viewsets.PromotersViewSet, basename="Promoters")
route.register(r'banks', viewsets.BanksViewSet, basename="Banks")
route.register(r'products', viewsets.ProductsViewSet, basename="Products")
route.register(r'customers', viewsets.CustomersViewSet, basename="Customers")
route.register(r'customerorigins', viewsets.CustomerOriginsViewSet, basename="CustomerOrigins")
route.register(r'customerservice', viewsets.CustomerServiceViewSet, basename="CustomerService")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    # Autenticação
    # path('token/', TokenObtainPairView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view()),
    # OpenAPI 3
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)