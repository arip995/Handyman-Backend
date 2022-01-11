from django.urls import path
from . import views

urlpatterns = [
    # path('details/',views.detail,{'id': 7})
    # path('details/',views.worker_list),
    path('details/',views.handymanadmin_details),
    path('signup/',views.handymanadmin_authentication),
    path('signin/',views.handymanadmin_authenticate),
    path('signinaccesstoken/<accessToken>/',views.handymanadmin_authenticateaccesstoken)
]