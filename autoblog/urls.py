from django.urls import path
from . import views

app_name = 'autoblog'

urlpatterns = [
    path('blog/', views.HomeView.as_view(), name='main'),
    path('category/<slug:slug>', views.BlogCategories.as_view(), name='category'),
    path('post/<slug:slug>', views.DetailPostView.as_view(), name='post'),
    path('my_posts/', views.UserPostsView.as_view(), name='my_posts'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),

]
