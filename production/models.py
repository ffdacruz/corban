from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, PROTECT
from uuid import uuid4
from validate_docbr import CPF


def upload_archives(instance, filename):
    return f'{instance.id_customer}-{filename}'


def cpf_validator(cpf):
    cpf = CPF()
    return cpf.validate(cpf)

class User(AbstractUser):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=15)
    birthday = models.DateField(null=True)
    certification_number = models.CharField(max_length=255)
    observation = models.TextField()

    def __str__(self):
        return self.get_short_name()   


class Products(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Banks(models.Model):
    id_bank = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.name


class Promoters(models.Model):
    id_promoter = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    banks = models.ManyToManyField(Banks)

    def __str__(self):
        return self.name


class CustomerOrigins(models.Model):
    id_customer_origin = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customers(models.Model):
    id_customer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    id_customer_origins = models.ForeignKey(CustomerOrigins, on_delete=models.PROTECT, related_name='customers')
    user = models.ForeignKey(User, on_delete=PROTECT, related_name='customers')
    customer_files = models.FileField(upload_to=upload_archives, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomerService(models.Model):
    class StatusService(models.IntegerChoices):
        SELECIONE = 1, 'Selecione uma opção'
        DIGITADO = 2, 'Digitado'
        FORMALIZANDO = 3, 'Formalizando'
        EM_ANDAMENTO = 4, 'Em Andamento'
        PENDENTE = 5, 'Pendente'
        PAGO = 6, 'Pago'
        REPROVADO = 7, 'Reprovado'
        CANCELADO = 8, 'Cancelado'


    id_customer_service = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    customer_origin = models.ForeignKey(CustomerOrigins, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    promoter = models.ForeignKey(Promoters, on_delete=models.PROTECT)
    bank = models.ForeignKey(Banks, on_delete=models.PROTECT)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    proposal_value = models.FloatField()
    proposal_number = models.CharField(max_length=255)
    date_service = models.DateField()
    status = models.CharField(max_length=30, null=False, blank=False, choices=StatusService.choices, default=StatusService.SELECIONE)
    observation = models.TextField()
    create_at = models.DateField(auto_now_add=True)