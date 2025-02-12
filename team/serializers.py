from rest_framework import serializers
from .models import *

class UIDesignersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIDesigners
        fields = '__all__'  


class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = '__all__'  

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'  

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'  

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'  

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'  