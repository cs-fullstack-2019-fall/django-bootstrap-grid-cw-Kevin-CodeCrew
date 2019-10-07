from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pages/<int:pgnum>/', views.generic_view, name="pages"),
]
