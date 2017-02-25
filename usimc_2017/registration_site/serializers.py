from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import (
    User,
)
from .models import (
    Entry,
    USIMCUser,
)
from rest_framework.fields import CurrentUserDefault


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)
    def create(self, validated_data):
            user = User.objects.create(**validated_data)
            usimc_user = USIMCUser.objects.create(user=user)
            return user

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('awards_applying_for' ,'instrument_category' ,'age_category' ,'submitted' ,'created_at' ,'updated_at')

class EntryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('instrument_category', 'age_category')
    def create(self, validated_data, usimc_user):
        validated_data['usimc_user'] = usimc_user
        return Entry.objects.create(**validated_data)

class USIMCUserSerializer(serializers.ModelSerializer):
    entries = serializers.ReadOnlyField()
    class Meta:
        model = USIMCUser
        fields = ('user', 'entries',)



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
