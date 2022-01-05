from django.db.models import fields
from rest_framework import serializers
from production import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class PromotersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promoters
        fields = '__all__'


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banks
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'


class CustomerOriginsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerOrigins
        fields = '__all__'


class CustomerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerService
        fields = '__all__'