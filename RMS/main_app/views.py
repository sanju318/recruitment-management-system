import random
from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status # import for login api
from django.contrib.auth.hashers import check_password #for hash password
from django.contrib.auth.hashers import make_password  #for hash password
from .models import UserInformation,Role,JobPost,InterviewScheduling,CandidateStatus,JobDesignation
from .serializers import LoginSerializer,SignupSerializer,UserSerializer,FilterSerializer
from utils.generateOTP import generate_otp
from utils.sendMail import send_html_email
# ,sendMail

#sign up api(using serializer)
class SignupAPIview(APIView):
    def post(self,request):
        serializer = SignupSerializer(data= request.data)
        
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
                password=hashed_password
                otp = generate_otp()
                profile_image = serializer.data.get("profile_image")
            subject = f"Your Verification Code is {otp}"
            html = html = f"""
                            <html>
                                <body style="margin: 0; padding: 0; background-color: #f1f3f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                    <div style="max-width: 600px; margin: 40px auto; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); overflow: hidden;">
                                    
                                    <div style="background-color: #1e88e5; padding: 20px 30px;">
                                        <h2 style="margin: 0; color: #ffffff; font-weight: 600; font-size: 24px;">
                                        RMS Email Verification
                                        </h2>
                                    </div>
                                    
                                    <div style="padding: 30px;">
                                        <p style="font-size: 16px; color: #333333;">Dear Candidate,</p>
                                        
                                        <p style="font-size: 15px; line-height: 1.6; color: #555;">
                                        Thank you for registering with the <strong style="color: #1e88e5;">Recruitment Management System (RMS)</strong>.
                                        To complete your registration and activate your account, please use the One-Time Password (OTP) below:
                                        </p>

                                        <div style="text-align: center; margin: 40px 0;">
                                        <span style="display: inline-block; padding: 16px 32px; background-color: #1e88e5; color: #ffffff; font-size: 28px; font-weight: bold; letter-spacing: 4px; border-radius: 8px;">
                                            {otp}
                                        </span>
                                        </div>

                                        <p style="font-size: 14px; color: #888888; text-align: center;">
                                        This OTP is valid for <strong>10 minutes</strong>. Please do not share it with anyone.
                                        </p>

                                        <p style="font-size: 14px; line-height: 1.6; color: #666;">
                                        If you did not request this verification, please disregard this email or contact our support team immediately.
                                        </p>

                                        <p style="margin-top: 40px; font-size: 15px; color: #333;">
                                        Warm regards,<br>
                                        <strong style="color: #1e88e5;">RMS Support Team</strong><br>
                                        Recruitment Management System
                                        </p>
                                    </div>

                                    <div style="background-color: #f1f3f5; text-align: center; padding: 15px; font-size: 12px; color: #999;">
                                        © 2025 Recruitment Management System. All rights reserved.
                                    </div>
                                    </div>
                                </body>
                                </html>
                           """
            send_html_email(subject,html,email)
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get all users

class UserAPIview(generics.ListAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserSerializer
#only candidate
class CandidateAPIView(generics.ListAPIView):
    queryset = UserInformation.objects.filter(role__name__iexact='candidate')
    serializer_class = UserSerializer
#only recruiter
class RecruiterAPIView(generics.ListAPIView):
    queryset = UserInformation.objects.filter(role__name__iexact='recruiter')
    serializer_class = UserSerializer
#only admin
class AdminAPIView(generics.ListAPIView):
    queryset = UserInformation.objects.filter(role__name__iexact='admin')
    serializer_class = UserSerializer


# login api
    
class LoginAPIView(APIView):
    def post(self,request):
        # print(data)
        serializer = LoginSerializer(data=request.data)
        print("===============================",serializer.is_valid())
        # print(serializer.is_valid())
        if serializer.is_valid():
            # print(serializer.data)
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            try:
                user = UserInformation.objects.get(username=username)        
                print(user)
                print("Password from request:", password)
                print("Password from DB:", user.password)

                if check_password(password,user.password):
                    
                    return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password "}, status=status.HTTP_401_UNAUTHORIZED)

            except UserInformation.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors }, status=status.HTTP_404_NOT_FOUND)
        

class FilterAPIView(generics.ListAPIView):
    serializer_class = FilterSerializer
    
    def get_queryset(self):
        username = self.request.query_params.get('username', '')
        return UserInformation.objects.filter(username__icontains=username)






# class FilterAPIView(APIView):
#     def get(self,request):
#         # name = request.GET.get('username', '')

#         # data = UserInformation.objects.filter(username__icontains=name).values()
#         # return Response(list(data))

#         id = request.GET.get('id', '')

#         data = UserInformation.objects.filter(id__icontains=id).values()
#         return Response(list(data))
    




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