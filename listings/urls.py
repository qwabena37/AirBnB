from django.urls import path
from . import views
from .views import HubtelMoMoPaymentView

urlpatterns = [
    path("", views.home, name="home"),                         # homepage
    path("properties/", views.PropertyListCreateView.as_view(), name="property-list"),
    path("properties/<int:pk>/", views.PropertyRetrieveView.as_view(), name="property-detail"),
       # ... your existing paths
    path("hubtel-momo/", HubtelMoMoPaymentView.as_view(), name="hubtel-momo"),
]
