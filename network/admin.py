from django.contrib import admin
from django.db.models import F
from django.utils.html import format_html

from .models import Factory, Product, Retailer, IndividualSeller, Network

admin.site.register(Network)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'release_date', 'date_created', 'manufacturer']
    list_filter = ['release_date', 'date_created', 'owner_factory']
    search_fields = ['name', 'model', 'owner_factory']

    @staticmethod
    def manufacturer(obj):
        if obj.owner_factory is not None:
            return format_html('<a href="{}">{}</a>'.format(obj.owner_factory.get_admin_url(), obj.owner_factory))
        return ''


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'supplier_link', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Retailers"

    def supplier_link(self, obj):
        if obj.parent is None:
            return ''
        return format_html('<a href="{}">{}</a>'.format(obj.parent.get_admin_url(), obj.parent))

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Supplier'


@admin.register(IndividualSeller)
class IndividualSellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'email', 'country', 'city', 'supplier_link', 'date_created']
    list_filter = ['country', 'city', 'street', 'house_number', 'date_created']
    search_fields = ['name', 'email', 'country', 'city', 'street', 'house_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'
    ordering = ['date_created', ]

    def clear_debt(self, _, queryset):
        queryset.update(dept_to_supplier=F('dept_to_supplier') * 0)

    clear_debt.short_description = "Clear Debt to Supplier For Selected Individual Sellers"

    def supplier_link(self, obj):
        if obj.parent is None:
            return ''
        return format_html('<a href="{}">{}</a>'.format(obj.parent.get_admin_url(), obj.parent))

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Supplier'
