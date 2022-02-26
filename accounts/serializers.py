from rest_framework import fields, serializers
from .models import accounts


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = accounts
        fields = ['id','first_name','last_name','company_name','city','state','zip','email','web','age']


class UserDetails(serializers.ModelSerializer):
    class Meta:
        model = accounts
        fields = ['id','first_name','last_name','company_name','city','state','zip','email','web','age']