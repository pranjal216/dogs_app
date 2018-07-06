from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create',views.create),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]