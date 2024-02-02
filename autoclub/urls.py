from django.urls import path
from . import views

app_name = 'autoclub'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('callback/', views.CallBackView.as_view(), name='callback'),

]