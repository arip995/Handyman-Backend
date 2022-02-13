from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.product_list),
    path('add-product/',views.add_product),
    path('edit-product/<id>/',views.edit_product),
]