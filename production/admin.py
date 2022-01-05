from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.forms import fields
from .forms import UserChangeForm, UserCreationForm
from production.models import User, Products, Banks, Promoters, CustomerOrigins, Customers, CustomerService


# Register your models here.

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Dados pessoais', {'fields':('cpf', 'rg', 'birthday', 'certification_number', 'observation',)}),
    )


admin.site.register(Products)
admin.site.register(Banks)
admin.site.register(Promoters)
admin.site.register(CustomerOrigins)
admin.site.register(Customers)
admin.site.register(CustomerService)