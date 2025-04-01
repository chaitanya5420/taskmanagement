from rest_framework.response import Response
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import  UserLoginSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache  # Used to store tokens temporarily
from rest_framework_simplejwt.exceptions import TokenError
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt


# def get_tokens_for_user(user):
#     """Reuse tokens if valid, generate new ones only when expired."""
    
#     existing_refresh = cache.get(f"user_refresh_{user.id}")
#     existing_access = cache.get(f"user_access_{user.id}")

#     try:
#         if existing_refresh:
#             refresh = RefreshToken(existing_refresh)
#             if refresh["exp"] > now().timestamp():
#                 if existing_access:
#                     access = AccessToken(existing_access)
#                     if access["exp"] > now().timestamp():
#                         return {'refresh': str(refresh), 'access': str(access)}

#                 access = refresh.access_token
#                 cache.set(f"user_access_{user.id}", str(access), timeout=300)  
#                 return {'refresh': str(refresh), 'access': str(access)}

#     except (TokenError, TypeError, KeyError):
#         pass

#     refresh = RefreshToken.for_user(user)
#     access = refresh.access_token

#     cache.set(f"user_refresh_{user.id}", str(refresh), timeout=120)  
#     cache.set(f"user_access_{user.id}", str(access), timeout=60)  

#     return {'refresh': str(refresh), 'access': str(access)}
  
  
  
  
class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]

  def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate data
        user = serializer.save()
        # token = get_tokens_for_user(user)

        # 🔹 Debugging: Print tokens in the console

        # 🔹 Return tokens in response
        return Response({
            'msg': 'Registration Successful'
        }, status=status.HTTP_201_CREATED)




# class UserProfileView(APIView):
#   renderer_classes = [UserRenderer]
#   permission_classes = [IsAuthenticated]
#   def get(self, request, format=None):
#     serializer = UserProfileSerializer(request.user)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# class UserChangePasswordView(APIView):
#   renderer_classes = [UserRenderer]
#   permission_classes = [IsAuthenticated]
#   def post(self, request, format=None):
#     serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
#     serializer.is_valid(raise_exception=True) # django-rf will automatically check serializer and raise validation error so no need for if
#     return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)


# class SendPasswordResetEmailView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = SendPasswordResetEmailSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


# class UserPasswordResetView(APIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, uid, token, format=None):
#     serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
#     serializer.is_valid(raise_exception=True)
#     return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

