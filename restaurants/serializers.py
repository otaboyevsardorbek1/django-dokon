from rest_framework import serializers


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    opens_at = serializers.TimeField(format="%H:%M")
    closes_at = serializers.TimeField(format="%H:%M")
