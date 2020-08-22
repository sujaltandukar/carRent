from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name="about"),
    path('car',views.car,name="car"),
    path('cardetail/<int:cid>', views.cardetail, name="car-detail"),
    path('book', views.book, name="book"),
    path('contact', views.contact, name="contact"),
    path('profile', views.profile, name="profile"),
    path('adminuser', views.adminuser, name="adminuser"),
    path('order/<int:cid>', views.order, name="order"),
    path('orderlist', views.orderlist, name="orderlist"),
    path('adminmsg', views.adminmsg, name="adminmsg"),
    path('search', views.search, name="search"),
    path('b_history/<int:id>', views.b_history, name="b_history"),
]