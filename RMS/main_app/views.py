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
                            <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 30px; color: #333;">
                                <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                                
                                <h2 style="color: #2d3436;">Recruitment Management System - Email Verification</h2>
                                
                                <p>Dear Candidate,</p>
                                
                                <p>Thank you for registering with the <strong>Recruitment Management System (RMS)</strong>. To complete your account setup and begin your journey with us, please use the following One-Time Password (OTP) to verify your email address:</p>
                                
                                <p style="font-size: 26px; font-weight: bold; color: #1e88e5; letter-spacing: 2px; text-align: center; margin: 30px 0;">{otp}</p>
                                
                                <p>This OTP is valid for <strong>10 minutes</strong>. Please do not share it with anyone.</p>
                                
                                <p>If you did not initiate this request, please ignore this email or contact our support team.</p>

                                <br>
                                <p>Warm regards,</p>
                                <p><strong>RMS Support Team</strong><br>
                                    Recruitment Management System</p>
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
        # print("===============================",serializer.is_valid())
        # print(serializer.is_valid())
        if serializer.is_valid():
            # print(serializer.data)
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            try:
                user = UserInformation.objects.get(username=username)        
                # print(user)
                if check_password(password,user.password):
                    return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password "}, status=status.HTTP_401_UNAUTHORIZED)

            except UserInformation.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": serializer.errors }, status=status.HTTP_404_NOT_FOUND)
        

# @api_view(["POST"]) 
# def generate_otp(request):
#     username = request.data.get("username")
    
#     try:
#         user = UserInformation.objects.get(username=username)
        
#         otp_code = str(random.randint(100000, 999999))
        
#         user_otp = otp_code
#         user.otp_created_at = timezone.now()
#         user.save()
        
#         print(f"otp sent to {user.username}:{otp_code}")

#         return Response({ 
#             "message": "OTP generated and stored successfully",
#             "username": user.username,
#             "otp": otp_code
#         }, status=status.HTTP_200_OK)
        
#     except UserInformation.DoesNotExist:
#         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

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