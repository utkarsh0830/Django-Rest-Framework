import django_filters
from .models import Item

class CustomFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(field_name='description',lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name',lookup_expr='iexact')
    id = django_filters.RangeFilter(field_name='id')
    class Meta:
        model = Item
        fields = ['description','name','id']
