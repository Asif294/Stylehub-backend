from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from  .import serializers
from  .import models
from rest_framework import viewsets,status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/user/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)
    
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid) 
       
    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active =True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

class UserloginApiView(APIView):
    
    def post(self,request):
        serializer =serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user= authenticate(username=username,password=password)
            if user:
                token, _ =Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({'error':"Invalid credential"})
        return Response(serializer.errors)
    
class UserLogoutView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer =serializers.UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = serializers.UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChangePasswordViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ChangePasswordSerializer
    model = User
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    