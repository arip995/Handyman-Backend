from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

urlpatterns = [
    # path('details/',views.detail,{'id': 7})
    path('details/',views.worker_list),
    path('signup/',views.worker_authentication),
    path('signin/',views.worker_authenticate)
    # path('details/',views.hello_world)

]