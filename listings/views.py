from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World — AirBnb Travel API. - built by James Try /properties/")

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer

class PropertyRetrieveView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

