from django.db import models

NULLABLE = {
    'null': True,
    'blank': True,
}


class Factory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Products', related_name='factory')

    class Products(models.Model):
        name = models.CharField(max_length=250, name='Product Name')
        model = models.CharField(max_length=250, name='Product Model')
        release_date = models.DateField()
        supplier = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL)
        dept_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


class Retailer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    products = models.ManyToManyField(Factory.Products, related_name='retailer')


class IndivodualSeller(models.Model):
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Factory.Products, related_name='indivodual_seller')
