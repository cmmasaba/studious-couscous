from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustomerViewSet
from orders.views import OrderViewSet

# using router to register viewsets and make the process of 
# generating the url consistent
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'orders', OrderViewSet, basename='order')

# API URLs will be determined automatically
urlpatterns = [
    path('', include(router.urls)),
]