from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'autoclub/index.html'
    extra_context = {
        'title': 'AutoClub'
    }


class AboutView(TemplateView):
    template_name = 'autoclub/about.html'
    extra_context = {
        'title': 'AutoClub'
    }


class CallBackView(TemplateView):
    template_name = 'autoclub/callback.html'
    extra_context = {
        'title': 'AutoClub'
    }
