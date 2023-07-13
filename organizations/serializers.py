from rest_framework import serializers
from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Organization
        fields = ['name','bio','creator', 'created_at']

    def create(self, validated_data):
       return Organization.objects.create(**validated_data)


class GetOrganizationSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Organization
        fields = ['id','name','bio','creator', 'created_at']