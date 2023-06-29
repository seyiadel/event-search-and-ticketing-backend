from rest_framework import serializers
from event_app.models import User, EventInfo
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 23, write_only = True)
    confirm_password = serializers.CharField(max_length = 23, write_only = True)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password','confirm_password',]
    
    def validate(self, attrs):
        user_email = attrs.get('email')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if user_email: 
            if User.objects.filter(email=user_email).exists():
                raise serializers.ValidationError(f"{user_email} already exists. Please Login.")
        if password and confirm_password:
            if password != confirm_password:
                raise serializers.ValidationError(f"Invalid Password!")
        return attrs
        
    def create(self, validated_data):
        return User.objects.create_user(first_name=validated_data['first_name'],last_name=validated_data['last_name'], email=validated_data['email'], password=validated_data['password'])

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=24, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            user_email = User.objects.get(email=email)
            if user_email:
                check_password = user_email.check_password(password)
                if check_password:
                    user = authenticate(request=self.context.get('request'), email=user_email, password=password)
                    if user is not None:
                        attrs['user'] = user
                        return attrs
                    else:
                        raise serializers.ValidationError("Invalid Credentials")
                else:
                    raise serializers.ValidationError("Incorrect Password")
            else:
                raise serializers.ValidationError("User do not exist, Please Sign up / Register ")
        raise serializers.ValidationError("Must contain email and password")


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = EventInfo
        fields = ['id','name','description', 'artwork','venue', 'location','country','type','start_time','start_date','end_time','end_date','created_at','organizer','earnings', 'is_published']

