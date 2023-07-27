from django.urls import path
from .views import *


app_name = "ecomapp"
urlpatterns = [

    # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/",AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),

    path("adminproductlist/", AdminProductListView.as_view(),name="adminproductlist"),
    path("adminproductadd/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),


]
