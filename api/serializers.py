from rest_framework import serializers
from .models import User


class UserSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    place = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    imgUri = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
