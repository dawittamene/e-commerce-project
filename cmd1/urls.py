
from django.urls import path
from .import views

urlpatterns = [
   
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('registration/', views.registrationpage, name="registration"),
    path('products/', views.products, name="products"),
    path('customer/', views.customer, name="customer"),
    path('order_form/', views.createorder, name="order_form"),
    path('update_order/<str:pk>/', views.updateorder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteorder, name="delete_order"),
   
   
]
