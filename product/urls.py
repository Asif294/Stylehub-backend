from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router=DefaultRouter()
router.register('brand',views.BrandViewset)
router.register('category',views.CategoryViewset)
router.register('size',views.SizeViewset)
router.register('product',views.ProductViewset)
router.register('review',views.ReviewViewset)
router.register('color',views.ColorViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('products/<int:pk>/', views.ProductsDetail.as_view(), name='Product_details'),
    # path('products/', ProductAPIView.as_view(), name='product-list'),
    # path('wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
