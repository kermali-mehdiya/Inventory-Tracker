from django.urls import path, include 
from . import views
from .views import export

urlpatterns = [
    path('', views.product_form,name='inventory_insert'),
    path('<int:id>/', views.product_form,name='inventory_update'),
    path('delete/<int:id>/',views.product_delete,name='inventory_delete'),
    path('list/',views.product_list, name='product_list'),
    path('export',export,name='export')
]


