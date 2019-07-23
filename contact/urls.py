from django.urls import path
from .views import contact_upload

urlpatterns = [
    path('', contact_upload, name='contact_upload')
]
