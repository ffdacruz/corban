from django_filters.rest_framework import DjangoFilterBackend
from production import models
from production.api import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework.filters import SearchFilter, OrderingFilter


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class PromotersViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.PromotersSerializer
    queryset = models.Promoters.objects.all()


class BanksViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.BanksSerializer
    queryset = models.Banks.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()


class CustomersViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.CustomersSerializer
    queryset = models.Customers.objects.all()


class CustomerOriginsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.CustomerOriginsSerializer
    queryset = models.CustomerOrigins.objects.all()


class CustomerServiceViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated)

    serializer_class = serializers.CustomerServiceSerializer
    queryset = models.CustomerService.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['proposal_number', 'id_customer', ]
    ordering = ['date_service']
    ordering_fields = ['date_service', 'status', 'id_promoter']