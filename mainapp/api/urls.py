from django.urls import path
from .api_views import (CategoryListApiView, BaseProductListApiView,
                        CustomersListAPIView, OrdersListAPIView, BaseProductApiView)

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    path('products/', BaseProductListApiView.as_view(), name='products'),
    path('products/<str:id>/', BaseProductApiView.as_view(), name='products_detail'),
    path('customers/', CustomersListAPIView.as_view(), name='customers_list'),
    path('orders/', OrdersListAPIView.as_view(), name='orders_list'),
]