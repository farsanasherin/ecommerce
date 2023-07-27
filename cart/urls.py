from django.urls import path
from .views import *


app_name = "ecomapp"
urlpatterns = [
path("", CustomerLoginView.as_view(), name="customerlogin"),
     path("register/",CustomerRegistrationView.as_view(), name="customerregistration"),
    # Client side pages
    path("home", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),

    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),

    path("checkout/", CheckoutView.as_view(), name="checkout"),
    
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),
]