from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    brand=models.CharField(max_length=50)

    def __str__(self):
        return self.brand

class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
class Size(models.Model):
    size=models.CharField(max_length=10)

    def __str__(self):
        return self.size

class Color(models.Model):
    color=models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Product(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="product/images/")
    body=models.TextField()
    price=models.CharField(max_length=50)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    size=models.ManyToManyField(Size)
    color=models.ManyToManyField(Color)
    
    def __str__(self):
        return self.title



    
STAR_CHOICE = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICE, max_length=5)

    def __str__(self):
        return str(self.id)
    
# class WishList(models.Model):
#     user = models.ForeignKey(User, related_name='wishlist', on_delete=models.CASCADE)
#     items = models.ManyToManyField(Product)

#     def __str__(self):
#         return self.user.first_name