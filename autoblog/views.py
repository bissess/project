from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import CreationPostForm, CommentForm
from .models import PostCategory, Post, Comment


class HomeView(ListView):
    template_name = 'autoblog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        # context['posts'] = Post.objects.annotate(comment_count=Count('comment'))
        return context


class UserPostsView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:sign_in')
    template_name = 'autoblog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class BlogCategories(ListView):
    template_name = 'autoblog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        return context


class DetailPostView(LoginRequiredMixin, DetailView, CreateView):
    login_url = reverse_lazy('users:sign_in')
    template_name = 'autoblog/detail_post.html'
    context_object_name = 'posts'
    form_class = CommentForm

    def get_queryset(self):
        return Post.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.get_object()
        return super().form_valid(form)

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        post = context['posts']
        context['count_comment'] = Comment.objects.filter(post=post).count()
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users:sign_in')
    template_name = 'autoblog/add_post.html'
    form_class = CreationPostForm
    success_url = reverse_lazy('autoblog:main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
