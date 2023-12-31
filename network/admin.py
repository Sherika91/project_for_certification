from django.contrib import admin

from network.models import Factory, Retailer, IndivodualSeller


@admin.register(Factory.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date']
    list_filter = ['release_date', 'created_at']
    search_fields = ['name', 'model']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at']
    list_filter = ['created_at', 'products', 'country', 'city', 'street', 'house_number']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]


@admin.register(Retailer)
class ReatailerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at', 'supplier',
                    'dept_to_supplier']
    list_filter = ['created_at', 'products', 'country', 'city', 'street', 'house_number']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]


@admin.register(IndivodualSeller)
class IndivodualSellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at', 'supplier',
                    'dept_to_supplier']
    list_filter = ['created_at', 'products', 'country', 'city', 'street', 'house_number']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]
