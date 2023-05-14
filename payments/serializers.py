from rest_framework import serializers
from payments.models import Checkout, BankDetail, WithdrawEventEarning
from tasks import verify_bank_details, create_tranfer_recipient

class CheckoutSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Checkout
        fields = "__all__"

    
class BankDetailSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BankDetail
        fields = "__all__"

    def create(self, validated_data):
        requested_account_number = validated_data['account_number']
        bank_code = validated_data['bank_code']
        # requested_account_name = validated_data['account_name']

        account_verify = verify_bank_details(requested_account_number, bank_code)
        print(account_verify)
        verified_account_name = account_verify["data"]["account_name"]
        verified_account_number = account_verify["data"]["account_number"]

        validated_data["account_name"] = verified_account_name

        transfer_receiver = create_tranfer_recipient(verified_account_name, verified_account_number, bank_code)
        receiver_code = transfer_receiver["data"]["recipient_code"]
        bank_name = transfer_receiver["data"]["details"]["bank_name"]
        
        validated_data["recipient_code"] = receiver_code
        validated_data["bank_name"] = bank_name
        
        return BankDetail.objects.create(**validated_data)


class WithdrawEventEarningSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    bank_detail = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = WithdrawEventEarning
        fields = "__all__"