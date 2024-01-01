from django.contrib import admin
from django.db.models import F
from network.models import Factory, Retailer, IndividualSeller


@admin.register(Factory.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'release_date']
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
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at',
                    'dept_to_supplier', 'get_supplier']
    list_filter = ['created_at', 'products', 'country', 'city', 'street', 'house_number']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]
    actions = ['clear_debt']

    def get_supplier(self, obj):
        return obj.supplier.name

    get_supplier.short_description = 'Supplier'

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Retailers"


@admin.register(IndividualSeller)
class IndividualSellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at',
                    'dept_to_supplier', 'get_supplier']
    list_filter = ['created_at', 'products', 'country', 'city', 'street', 'house_number']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ['created_at', ]
    actions = ['clear_debt']

    def get_supplier(self, obj):
        return obj.supplier.name

    get_supplier.short_description = 'Supplier'

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Individual Sellers"
