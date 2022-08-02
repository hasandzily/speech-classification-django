from django.urls import path

from . import views

app_name = 'tugas2_1301194367'

urlpatterns = [
    path('', views.index, name='index'),
]