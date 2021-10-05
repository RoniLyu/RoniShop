from rest_framework import serializers

from ..models import Product, Category, Order, Customer


class CategorySerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)
    # category = serializers.SlugRelatedField(slug_field='name',
    #                                         queryset=Category.objects.all())
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]

class BaseProductSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=False)
    description = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:

        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)

    class Meta:
        model = Customer
        fields = '__all__'


# class CartSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Cart
#         fields = '__all__'