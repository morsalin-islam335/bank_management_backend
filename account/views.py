from django.shortcuts import render, redirect
from django.http import HttpResponse
from .serializers import AccountSerializer, AddressSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView

############# Import necessary models #########
from .models import UserBankAccount, UserAddress
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken


from . serializers import  UserLoginSerializer

####################### Generate Secure Token For User Registration ##################
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes



############################ Email Sending######################
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
################# Authentication and Authorization #######
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token


# class UserRegistrationApiView(APIView):
#     serializer_class = UserRegistrationSerializer
    
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             # user = serializer.save()
#             # print(user)
#             # token = default_token_generator.make_token(user)
#             # print("token ", token)
#             # uid = urlsafe_base64_encode(force_bytes(user.pk))
#             # print("uid ", uid)
#             # # confirm_link = f"https://smart-care.onrender.com/patient/active/{uid}/{token}"
#             # confirm_link = f"http://127.0.0.1:8000/account/active/{uid}/{token}"
#             # email_subject = "Confirm Your Email"
#             # email_body = render_to_string('confirmation_email.html', {'confirm_link' : confirm_link})
            
#             # email = EmailMultiAlternatives(email_subject , '', to=[user.email])
#             # email.attach_alternative(email_body, "text/html")
#             # email.send()
#             # return Response("Check your mail for confirmation")
#         return Response(serializer.errors)


class UserAccountCreateSerializer(APIView):
    serializer_class = AccountSerializer

    def post(self, request):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("account set")
        return Response(serializer.errors)

class UserAddressCreateSerializer(APIView):
    serializer_class = AddressSerializer
    def post(self, request):
        serializer = AddressSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("address set")
        return Response(serializer.errors)




#################### Authentication and Authorization works ###########
    


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Your account is activated")
    else:
        return HttpResponse("You make wrong")

    

class UserLoginApiView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)


class UserLogoutAPIView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
         # return redirect('login')
        return Response({'success' : "logout successful"})
    


