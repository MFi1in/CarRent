from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('про_нас', views.about, name='about'),
    path('автопарк', views.car, name='car'),
    path('подписка', views.sub, name='sub'),
]