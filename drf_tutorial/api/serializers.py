from rest_framework import serializers
from .models import Item,Order

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only = True)
    class Meta:
        model = Order
        fields = '__all__'