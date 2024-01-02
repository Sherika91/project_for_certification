from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

NULLABLE = {
    'null': True,
    'blank': True,
}


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=50)
    release_date = models.DateField()
    owner = models.ForeignKey('Network', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.model}, {self.release_date}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['name', 'model', 'release_date'])
        ]


class Network(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    dept_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    parent = TreeForeignKey('self', **NULLABLE, related_name='childeren', db_index=True, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['name', 'slug', 'email', 'country', 'city']),
        ]


class Factory(Network):
    class Meta:
        verbose_name = 'Factory'
        verbose_name_plural = 'Factories'
        ordering = ['-date_created']


class Retailer(Network):
    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'
        ordering = ['-date_created']


class IndividualSeller(Network):
    class Meta:
        verbose_name = 'Individual Seller'
        verbose_name_plural = 'Individual Sellers'
        ordering = ['-date_created']
