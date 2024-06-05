from urllib.parse import uses_relative
from accounts.models import UserProfile
from vendor.models import Vendor
from django.conf import settings


#---context processors are useful for adding common data to every template without the need to manually include that data in every view.Create a new Python file, e.g., context_processors.py, in one of your Django apps,In your Django settings file, add the path to your custom context processor to the TEMPLATES setting:In your templates, you can now use the variable provided by the context processor: 

def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except:
        vendor = None
    return dict(vendor=vendor)


def get_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None
    return dict(user_profile=user_profile)


#google api setup(we put below 2 code in secure file .env and we need these id in google api CDN and paypal CDN in base.html so we write these key here we already know that context processor content can access in all file)
def get_google_api(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}


def get_paypal_client_id(request):
    return {'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID}