from django.contrib import admin

from .models import Brand,Category,Product,Size,Review,Color
class ReviewAdmin(admin.ModelAdmin):
    list_display=['reviewer','product','rating']

class SizeAdmin(admin.ModelAdmin):
    list_display=['size']

class ColorAdmin(admin.ModelAdmin):
    list_display=['color']

class BrandAdmin(admin.ModelAdmin):
    list_display=['brand']
      
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category']

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','image']
admin.site.register(Brand,BrandAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Review,ReviewAdmin)


