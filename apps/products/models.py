from django.db import models

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='products name'
    )
    descriptions = models.TextField(
        verbose_name='product description'
    )
    price = models.FloatField(
        default=0,
        verbose_name="product price"
    )
    amount = models.IntegerField(
        default=1,
        verbose_name='product quantity',
        blank=True, null=True
    )
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Product settings"
        
        
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Products image" 
        