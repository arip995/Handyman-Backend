from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
from . import viewsInformation

urlpatterns = [
    path('details/',views.worker_list),
    path('signup/',views.worker_authentication),
    path('signin/',views.worker_authenticate),
    path('signinaccesstoken/',views.worker_authenticateaccesstoken),
    path('detail/<id>/',views.get_worker_details_by_id),
    path('add/information/',viewsInformation.add_worker_information),
    path('update/information/<id>/',viewsInformation.update_worker_information),
    path('update/info/<id>/',views.worker_update)
]