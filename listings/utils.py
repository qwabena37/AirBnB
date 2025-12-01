import requests
from django.conf import settings

def get_hubtel_access_token():
    url = "https://api.hubtel.com/oauth/token"
    data = {
        "client_id": settings.HUBTEL_CLIENT_ID,
        "client_secret": settings.HUBTEL_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()['access_token']
