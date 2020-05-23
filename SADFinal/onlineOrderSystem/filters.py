from django.contrib.auth.models import User
from onlineOrderSystem.models import OrderForm, Staff
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['IDName']

class OrderFormFilter(django_filters.FilterSet):
    class Meta:
        model = OrderForm
        fields = ['IDName']