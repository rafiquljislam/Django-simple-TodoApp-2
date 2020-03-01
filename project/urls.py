from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name='add'),
    path('delete/<int:num>/',views.deleta,name='delete'),
    path('update/<int:num>/',views.update,name='delete'),
]
