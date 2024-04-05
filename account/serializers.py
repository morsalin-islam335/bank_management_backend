import random


from rest_framework import serializers
from .models import UserBankAccount, UserAddress

from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

GENDER_TYPE = (
    ("MALE", "MALE"),
    ("FEMAlE", "FEMAlE")
)

ACCOUNT_TYPE = (
    ("CURRENT", "CURRENT"),
    ("SAVINGS", "SAVINGS")
)

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     birth_date = serializers.DateField()
#     gender = serializers.ChoiceField(choices=GENDER_TYPE)
#     account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE)
#     street_address = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length= 100)
#     postal_code = serializers.IntegerField()
#     country = serializers.CharField(max_length=100)
#     password1 = serializers.CharField(write_only = True)
#     password2 = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date','gender', 'postal_code', 'city','country', 'street_address']
        
#         # form.save()
#         '''
#     def save(self, commit=True):
#         our_user = super().save(commit=False) # ami database e data save korbo na ekhn
#         if commit == True:

#             if self.validated_data.get('password') != self.validated_data.get('password2'):
#                 raise serializers.ValidationError("Passwords and confirm password does not match not match")

#             our_user.is_active = False # after clicking activation link it will be active otherwise not
#             our_user.save() # user model e data save korlam
#             account_type = self.validated_data.get('account_type')
#             gender = self._validated_data.get('gender')
#             postal_code = self._validated_data.get('postal_code')
#             country = self._validated_data.get('country')
#             birth_date = self._validated_data.get('birth_date')
#             city = self._validated_data.get('city')
#             street_address = self._validated_data.get('street_address')
            
#             UserAddress.objects.create(
#                 user = our_user,
#                 postal_code = postal_code,
#                 country = country,
#                 city = city,
#                 street_address = street_address
#             )
#             UserBankAccount.objects.create(
#                 user = our_user,
#                 account_type  = account_type,
#                 gender = gender,
#                 birth_date =birth_date,
#                 account_no = 100000+ our_user.id
#             )

# '''

#     def create(self, validated_data):
#         ############ User address information #############
#         postal_code = validated_data.pop('postal_code')
#         country = validated_data.pop('country')
#         city = validated_data.pop('city')
#         street_address = validated_data.pop('street_address')
    
#         ################ User account information ##############
    
#         account_no = 121+random.randint(1000,20000)
#         account_type = validated_data.pop('account_type')
#         gender = validated_data.pop('gender')
#         birth_date = validated_data.pop('birth_date')
    
        
#         username = validated_data.get("username")
#         first_name = validated_data.get("first_name")
#         last_name= validated_data.get("last_name")
#         email= validated_data.get("email")

#         password1 = validated_data.pop('password1')
#         password2 = validated_data.pop('password2')
        
#         if password1 != password2:
#             raise serializers.ValidationError("Passwords do not match")

#         user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email)

#         UserAddress.objects.create(user=user, street_address = street_address, city = city, postal_code = postal_code, country = country)
#         UserBankAccount.objects.create(user=user, account_type = account_type, account_no = account_no, birth_date = birth_date, gender = gender)

        
        


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


