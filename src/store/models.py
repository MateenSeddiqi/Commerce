from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    NUMBER_CHOICES = [(i, str(i)) for i in range(1,201)]
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.IntegerField(null=True, default=0)
    name = models.CharField(max_length=100)
    package_contain = models.PositiveBigIntegerField(choices=NUMBER_CHOICES)
    package_purchase_price = models.IntegerField(default=0, null=True)
    total_package_price = models.IntegerField(default=0, null=True)     
    num_of_packages = models.IntegerField(default=1)
    package_sale_price = models.IntegerField(null=True, default=0)
    item_sale_price = models.IntegerField( null=True ,default=0)
    total_items = models.IntegerField(null=True,default=0)
    image = models.ImageField(default='default.svg', upload_to='item_images')
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name