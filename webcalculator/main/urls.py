from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('convert/<str:number>/<int:start_system>/<int:end_system>', views.Convert.as_view(), name='convert'),
    path('', views.translate, name='main_page'),
    path('calculate/<str:first_number>/<int:first_number_start_system>/<str:second_number>/'
         '<int:second_number_start_system>/<str:oper>', views.Calculate.as_view(), name='calculate'),
    path('calculate/<str:first_number>/<int:first_number_start_system>/<str:second_number>/'
         '<int:second_number_start_system>/<str:oper>/<int:end_system>', views.Calculate.as_view(), name='calculate'),
    path('calculator/', views.calculator, name='calculator'),
]

urlpatterns += staticfiles_urlpatterns()
