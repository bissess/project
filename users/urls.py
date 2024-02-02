from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('sign_in/', views.UserLoginView.as_view(), name='sign_in'),
    path('sign_up/', views.UserRegistrationView.as_view(), name='sign_up'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
    path('profile/safety', views.ProfileSafetyView.as_view(), name='safety'),

    path('reset-password/', views.UserPasswordResetView.as_view(), name='password-reset'),
    path('reset-password/done/', views.UserPasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset-password/confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset-password/complete/', views.UserPasswordResetCompleteView.as_view(), name='password-reset-complete'),
]