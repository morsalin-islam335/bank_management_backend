from django.shortcuts import render

# Create your views here.

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . serializers import TransactionSerializers
from rest_framework import viewsets

from . models import Transaction
from rest_framework.response import Response

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()




class TransactionViewSets(viewsets.ModelViewSet):
        serializer_class = TransactionSerializers
        queryset = Transaction.objects.all()

        
        def post(self, request):
                serializer = self.serializer_class(data = request.post)
                if serializer.is_valid():
                        serializer.save()
                        return Response({"OK": "done"})

                else:
                    return serializer.errors()
