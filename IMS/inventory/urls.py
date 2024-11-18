# inventory/urls.py
from django.urls import path
from inventory import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("products/", views.products, name="products"),
    path("orders/", views.orders, name="orders"),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),#ログアウト用に追加
]

