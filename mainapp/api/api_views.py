from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from .serializers import (CategorySerializer, BaseProductSerializer,
                          CustomerSerializer, OrderSerializer
                          )
from ..models import Category, Product, Customer, Order


class Pagination(PageNumberPagination):

    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3

class CategoryListApiView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BaseProductListApiView(ListAPIView):

    serializer_class = BaseProductSerializer
    pagination_class = Pagination
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

class BaseProductApiView(RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView):

    serializer_class = BaseProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class CustomersListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    pagination_class = Pagination
    queryset = Customer.objects.all()


class OrdersListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = Pagination
    queryset = Order.objects.all()