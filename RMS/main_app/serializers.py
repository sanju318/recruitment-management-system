from rest_framework import serializers  
from main_app.models import UserInformation,Role
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # class Meta :
    #     model = UserInformation
    #     fields = ['username','password']

class SignupSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserInformation
        fields = ['username','email','phone','password','otp','role']
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def validate(self,attr):
        print("===========",attr)

        email = attr.get("email")
        user = UserInformation.objects.filter(email=email,is_verified=1)

        if user:
            raise ValidationError("User is already registered")
        return attr
        
    
class UserSerializer(serializers.ModelSerializer):
    # role_name = serializers.SerializerMethodField()
    role_name = serializers.CharField(source="role.name", read_only=True) # we can use this instead of serializersMethodfield()

    class Meta:
        model = UserInformation
        fields = "__all__"
        # exclude = ["password","created_at"]
    # def get_role_name(self, obj): # if we use (source="role.name", read_only=True) so don't need to write (get_role_name(self, obj) this method
    #     return obj.role.name

class FilterSerializer(serializers.ModelSerializer):      #filter_by
    class Meta :
        model = UserInformation
        fields = "__all__"