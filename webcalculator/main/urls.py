from django.urls import path
from . import views

urlpatterns = [
    path('convert/<str:number>/<int:start_system>/<int:end_system>', views.Convert.as_view(), name='convert'),
    path('', views.main_page, name='main_page'),
]
