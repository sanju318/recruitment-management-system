import random
from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status # import for login api
from django.contrib.auth.hashers import make_password , check_password #for hash password
from .models import UserInformation,Role
from .serializers import LoginSerializer,SignupSerializer,UserSerializer
from utils.generateOTP import generate_otp
from utils.sendMail import send_html_email


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserSerializer

#sign up api
def create(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # hash password
            raw_password = data.get("password")
            print("Before",raw_password)
            hashed_password = make_password(raw_password)
            print("After",hashed_password)

            # check role
            try:
                role_id = data.get("role")
                role = Role.objects.get(id=role_id)
            except Role.DoesNotExist:
                return Response({"error": "Invalid role ID"}, status=status.HTTP_400_BAD_REQUEST)

            username = data.get("username")
            email = data.get("email")
            phone = data.get("phone")
            profile_image = data.get("profile_image")
            password=password
            otp = generate_otp()

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
                    password = hashed_password,
                    otp=otp,
                    role=role,
                    profile_image=profile_image
                )

            return Response({"message": "User created", "user_id": user.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# login api
@action(detail=False, methods=["post"], url_path="login")
def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            try:
                user = UserInformation.objects.get(username=username)
                if check_password(password, user.password):
                    return Response({"message": "Login successful", "username": user.username})
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            except UserInformation.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)