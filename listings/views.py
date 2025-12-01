from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
import uuid
from .utils import get_hubtel_access_token  # import helper


def home(request):
    return HttpResponse("Hello World — AirBnb Travel API. - built by James Try /properties/")

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer

class PropertyRetrieveView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


# add filter backend
    filter_backends = [DjangoFilterBackend]

    # fields you want to be able to filter by
    filterset_fields = ['city', 'available']

class HubtelMoMoPaymentView(APIView):
    def post(self, request):
        amount = request.data.get("amount")  # e.g., "10.00"
        mobile_number = request.data.get("mobile_number")  # e.g., "0244123456"
        currency = request.data.get("currency", "GHS")  # Ghanaian Cedi
        reference = str(uuid.uuid4())  # unique payment reference
        description = request.data.get("description", "Property Booking Payment")

        if not amount or not mobile_number:
            return Response({"error": "Amount and mobile number are required"}, status=status.HTTP_400_BAD_REQUEST)

        access_token = get_hubtel_access_token()

        url = "https://api.hubtel.com/v1/merchantpayments/mobilemoney/gh/paymentrequest"
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "MerchantId": settings.HUBTEL_MERCHANT_ID,
            "CustomerMsisdn": mobile_number,
            "Amount": amount,
            "CurrencyCode": currency,
            "TransactionReference": reference,
            "CallbackUrl": "https://yourdomain.com/hubtel/payment/callback/",
            "Reason": description,
            "Metadata": {
                "Product": "Jay AirBnB Booking"
            }
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({
                "error": "Payment request failed",
                "details": response.json()
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_home(request):
    return Response({
        "message": "Welcome to Jay AirBnB API",
        "endpoints": {
            "properties": "/properties/",
            "payment": "/hubtel-momo/",
            "swagger": "/swagger/",
            "admin": "/admin/"
        }
    })