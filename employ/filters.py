import django_filters
from django_filters import CharFilter

from .models import *

class EmployeeFilter(django_filters.FilterSet):

    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')

    class Meta:
        model = Employee
        fields = ['name', 'department']