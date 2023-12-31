from django.db import models

NULLABLE = {
    'null': True,
    'blank': True,
}


class Factory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Products', related_name='factory_products')

    class Products(models.Model):
        name = models.CharField(max_length=250)
        model = models.CharField(max_length=250)
        release_date = models.DateField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"{self.name}, {self.model}, {self.release_date}"

        class Meta:
            verbose_name = 'Products'
            verbose_name_plural = 'Products'
            ordering = ['-created_at']
            indexes = [
                models.Index(fields=['name', 'model', 'release_date'])
            ]

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = 'Factory'
        verbose_name_plural = 'Factories'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name', 'slug', 'email', 'country', 'city']),
        ]


class Retailer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='retailer_supplier')
    dept_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    products = models.ManyToManyField(Factory.Products, related_name='retailer_products')

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = 'Retailer'
        verbose_name_plural = 'Retailers'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['name', 'slug', 'email', 'country', 'city'])
        ]


class IndivodualSeller(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='individual_seller_supplier')
    dept_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    products = models.ManyToManyField(Factory.Products, related_name='indivodual_seller_products')

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}, {self.city}"

    class Meta:
        verbose_name = 'IndivodualSeller'
        verbose_name_plural = 'IndivodualSellers'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name', 'slug', 'email', 'country', 'city'])
        ]