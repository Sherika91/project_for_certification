from django.contrib import admin
from django.db.models import F

from .models import Factory, Product, Retailer, IndividualSeller


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'release_date', 'date_created', 'owner']
    list_filter = ['release_date', 'date_created']
    search_fields = ['name', 'model']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]


@admin.register(Retailer)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Retailers"


@admin.register(IndividualSeller)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Individual Sellers"
