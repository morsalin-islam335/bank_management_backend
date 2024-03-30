from rest_framework import serializers
from .models import UserBankAccount, UserAddress

from django.contrib.auth.models import User

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserBankAccount
#         fields = '__all__'


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAddress
#         fields = '__all__'

GENDER_TYPE = (
    ("MALE", "MALE"),
    ("FEMAlE", "FEMAlE")
)

ACCOUNT_TYPE = (
    ("CURRENT", "CURRENT"),
    ("SAVINGS", "SAVINGS")
)

class UserRegistrationSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField()
    gender = serializers.ChoiceField(choices=GENDER_TYPE)
    account_type = serializers.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length= 100)
    postal_code = serializers.IntegerField()
    country = serializers.CharField(max_length=100)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date','gender', 'postal_code', 'city','country', 'street_address']
        
        # form.save()
    def save(self, commit=True):
        our_user = super().save(commit=False) # ami database e data save korbo na ekhn
        if commit == True:

            if self.validated_data.get('password') != self.validated_data.get('password2'):
                raise serializers.ValidationError("Passwords and confirm password does not match not match")

            our_user.is_active = False # after clicking activation link it will be active otherwise not
            our_user.save() # user model e data save korlam
            account_type = self.validated_data.get('account_type')
            gender = self._validated_data.get('gender')
            postal_code = self._validated_data.get('postal_code')
            country = self._validated_data.get('country')
            birth_date = self._validated_data.get('birth_date')
            city = self._validated_data.get('city')
            street_address = self._validated_data.get('street_address')
            
            UserAddress.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
            )
            UserBankAccount.objects.create(
                user = our_user,
                account_type  = account_type,
                gender = gender,
                birth_date =birth_date,
                account_no = 100000+ our_user.id
            )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)