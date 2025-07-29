from rest_framework import serializers
from main_app.models import UserInformation,Role
from rest_framework.exceptions import ValidationError

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20,required=True)
    password = serializers.CharField(max_length=20,required=True)

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20,required=True)
    email = serializers.EmailField(max_length=250,required=True)
    phone = serializers.CharField(max_length=25,required=True)
    password = serializers.CharField(max_length=50,required=True)
    otp = serializers.CharField(max_length=6,required=True)
    role = serializers.CharField(max_length=20,required=True)
    
    def validate(self,attr):
        print(attr)
        role_id = attr.get("role")
        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            raise ValidationError("Invalid role ID")

        if role.name.lower() != "candidate":
            raise ValidationError("User is not a candidate")
        return attr
        
    
class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()
    class Meta:
        model = UserInformation
        # fields = "__all__"
        exclude = ["password","created_at"]
    def get_role_name(self, obj):
        return obj.role.name