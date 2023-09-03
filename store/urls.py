from django.urls import path
from . import views





urlpatterns = [
    path('', views.store, name="store"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("detail/<int:item_id>",views.detail,name="detail"),
    path("categ/<str:name>",views.categ,name="categ"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order")
]