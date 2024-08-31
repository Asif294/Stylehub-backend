from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views
router=DefaultRouter()

router.register('password_change', views.ChangePasswordViewSet, basename='password_change')

urlpatterns = [
    path('',include(router.urls)),
    path('user/<int:id>/', views.UserProfileDetail.as_view(), name='user-details'),
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('login/',views.UserloginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate,name='activate')
]
