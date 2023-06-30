from rest_framework import serializers
from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Organization
        fields = "__all__"

    def create(self, validated_data):
       return Organization.objects.create(**validated_data)

