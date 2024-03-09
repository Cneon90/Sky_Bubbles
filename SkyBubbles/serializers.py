from django.contrib.auth.models import Group, User
from rest_framework import serializers
from SkyBubbles.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'color', 'size_h','size_w', 'weight','category', 'description']


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ['name', 'description']


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'description', 'created_date']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['price_delivery', 'created_date']


class AcceptanceSerializer(serializers.HyperlinkedModelSerializer):
    Transaction = serializers.PrimaryKeyRelatedField(
        queryset=Transaction.objects.all())
    ingredient = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())
    storage = serializers.PrimaryKeyRelatedField(
        queryset=Storage.objects.all())
    partner = serializers.PrimaryKeyRelatedField(
        queryset=Partner.objects.all())

    class Meta:
        model = Acceptance
        fields = '__all__'
        # fields = ['ingredient', 'storage', 'partner', 'count', 'price', 'active', 'created_date']




