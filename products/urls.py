from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewset


app_name = 'api'

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewset, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
