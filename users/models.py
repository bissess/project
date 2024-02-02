from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = {
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    }

    photo = models.ImageField(upload_to='users/user_photo', blank=True, null=True,
                              default='users/user_photo/default_image.png', verbose_name='Изображение пользователя')
    date_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, verbose_name='Пол')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})