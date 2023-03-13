from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyDesignItemView.as_view(), name='my_design_item_list'),     # for listing and creating
    path('<int:pk>', views.MyDesignItemView.as_view(), name='item_detail'),     # for detail, updating, and deleting
]
