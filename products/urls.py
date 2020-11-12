from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.productHome, name="prod_home"),
    path('list/', views.productList, name="prod_list"),
    path('more/<str:P_id>/', views.productMore, name="prod_more"),
]