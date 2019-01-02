from django.conf.urls import url, include
from API import views

urlpatterns = [
    url(r'asset/', views.asset)
]