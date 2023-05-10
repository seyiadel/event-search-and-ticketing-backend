from rest_framework import serializers
from payments.models import Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Checkout
        fields = "__all__"

    