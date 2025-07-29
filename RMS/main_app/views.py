import random
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status # import for login api 
from django.contrib.auth.hashers import check_password #for hash password
from django.contrib.auth.hashers import make_password  #for hash password
from .models import UserInformation,Role,JobPost,InterviewScheduling,CandidateStatus,JobDesignation
from .serializers import LoginSerializer,SignupSerializer,UserSerializer





#sign up api(using serializer)
class SignupAPIview(APIView): 
    def post(self,request):
        data=request.data
        serializer = SignupSerializer(data= data)
        
        if serializer.is_valid():
            data = serializer.data
            
            raw_password = data.get("password")  #for hash password
            hashed_password = make_password(data.get(raw_password)) #for hash password

            try:
                role_id = data.get("role")  # should be a string or int
                role = Role.objects.get(id=role_id)
            except Role.DoesNotExist:
                return Response({"error": "Invalid role ID"}, status=400)  

            # Extract other fields
            if serializer.is_valid():
                print(serializer.data)
                username = serializer.data.get("username")
                email = serializer.data.get("email")
                phone = serializer.data.get("phone")
                password=hashed_password    ,
                otp = serializer.data.get("otp")
                profile_image = serializer.data.get("profile_image")

            # data for Create user
            user = UserInformation.objects.create(
                username=username,
                email=email,
                phone=phone,
                password=password,
                otp=otp,
                role=role,
                profile_image=profile_image
            )

            return Response({"message": "User created", "user_id": user.id})
from rest_framework import generics
class UserAPIview(generics.ListAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserSerializer
# login api
    
@api_view(["POST"]) 
def login(request):
    data = request.data
    # print(data)
    serializer = LoginSerializer(data=data)
    # print(serializer.is_valid())
    if serializer.is_valid():
        # print(serializer.data)
        username = serializer.data.get("username")
        password = serializer.data.get("password")

        try:
            user = UserInformation.objects.get(username=username)        
            if check_password(password,user.password):
                return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

        except UserInformation.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["POST"]) 
def generate_otp(request):
    username = request.data.get("username")
    
    try:
        user = UserInformation.objects.get(username=username)
        
        otp_code = str(random.randint(100000, 999999))
        
        user_otp = otp_code
        user.otp_created_at = timezone.now()
        user.save()
        
        print(f"otp sent to {user.username}:{otp_code}")

        return Response({
            "message": "OTP generated and stored successfully",
            "username": user.username,
            "otp": otp_code
        }, status=status.HTTP_200_OK)
        
    except UserInformation.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
def filter_by(request):
    # name = request.GET.get('username', '')

    # data = UserInformation.objects.filter(username__icontains=name).values()
    # return Response(list(data))

    id = request.GET.get('id', '')

    data = UserInformation.objects.filter(id__icontains=id).values()
    return Response(list(data))
    




#get all user

# @api_view(["GET"])
# def Recruiterview(request):
#     method = request.method
#     if method == "GET":
#         #data = UserInformation.objects.all()
#         userdata = UserInformation.objects.all()
#         stf  = []
#         print(request.method)
#         for i in userdata:
#             l = {"name":i.username,"email":i.email} #create dictionaty to show json data in postman
#             stf.append(l)
#         return Response(stf)


#sign up api

# @api_view(["POST"]) 
# def signup(request):
#     data = request.data.copy()  # make a mutable copy
    
#     raw_password = data.get("password")  #for hash password
#     hashed_password = make_password(data.get(raw_password)) #for hash password

#     try:
#         role_id = data.get("role")  # should be a string or int
#         role = Role.objects.get(id=role_id)
#     except Role.DoesNotExist:
#         return Response({"error": "Invalid role ID"}, status=400)  

#     # Extract other fields
#     username = data.get("username")
#     email = data.get("email")
#     phone = data.get("phone")
#     password=hashed_password,
#     otp = data.get("otp")
#     profile_image = request.FILES.get("profile_image")

#     # Create user
#     user = UserInformation.objects.create(
#         username=username,
#         email=email,
#         phone=phone,
#         password=password,
#         otp=otp,
#         role=role,
#         profile_image=profile_image
#     )

#     return Response({"message": "User created", "user_id": user.id})