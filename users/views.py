from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView

from .forms import UserAuthForm, UserRegForm, UserProfileForm, ProfileSafetyForm, UserPasswordResetForm, \
    UserPasswordResetConfirmForm
from autoblog.models import Post, Comment


class UserLoginView(LoginView):
    template_name = 'users/sign_in.html'
    form_class = UserAuthForm


class UserRegistrationView(CreateView):
    template_name = 'users/sign_up.html'
    form_class = UserRegForm
    success_url = reverse_lazy('users:sign_in')

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = 'Регистрация прошла успешно'
        message = 'Дорогой пользователь. Мы рады видеть вас, в кругу нашей дружественной общины.' \
                  'Спасибо вам за регистрацию! Ваш BMW AutoClub.'
        from_email = 'bisenov2002@list.ru'
        to_email = form.cleaned_data['email']

        send_mail(subject, message, from_email, [to_email])

        return response


class UserLogoutView(LogoutView):

    def get_success_url(self):
        return reverse_lazy('users:sign_in')


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('users:password-reset-done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    form_class = UserPasswordResetConfirmForm
    success_url = reverse_lazy('users:password-reset-complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    model = get_user_model()
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        post_count = Post.objects.filter(author=user).count()
        comment_count = Comment.objects.filter(user=user).count()

        context['post_count'] = post_count
        context['comment_count'] = comment_count
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile')


class ProfileSafetyView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/safety.html'
    model = get_user_model()
    form_class = ProfileSafetyForm
    success_url = reverse_lazy('users:profile')
