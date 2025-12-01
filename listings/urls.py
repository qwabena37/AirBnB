from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),                         # homepage
    path("properties/", views.PropertyListCreateView.as_view(), name="property-list"),
    path("properties/<int:pk>/", views.PropertyRetrieveView.as_view(), name="property-detail"),
]
