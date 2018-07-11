from django.urls import path
from django.contrib.auth import views as loginview
from Controller.forms import LoginForm
from . import views

urlpatterns = [
        path('login/',loginview.login,{'authentication_form':LoginForm}),
        path('',views.home,name='Home'),
        path('draw/',views.drawTopology,name='Draw'),
]
