from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
  path(
    'cms/blog/',
    views.CMSPostListView.as_view(),
    name='cms_blog'
  ),
  path(
    'posts/',
    views.PostListView.as_view(),
    name='posts_list'
  ),
  path(
    'posts/<slug:category_slug>/',
    views.PostListView.as_view(),
    name='posts_list_by_category'
  ),
  path(
    'post/<int:pk>/details/',
    views.PostDetailView.as_view(),
    name='post_details'
  ),
  path(
    'post/create/', 
    views.PostCreateView.as_view(), 
    name='create_post'
  ),
  path(
    'post/<slug:post_slug>/update/',
   	views.PostUpdateView.as_view(), 
    name='update_post'
  ),
  path(
    'post/<slug:post_slug>/<str:action>/',
   	views.TrashUnTrashArticle.as_view(), 
    name='trash_or_restore'
  ),
  path(
    'trash/list/', 
    views.TrashListView.as_view(), 
    name='open_trash'
  ),
  path(
    'trash/empty/', 
    views.EmptyBlogTrashView.as_view(),
   	name='empty_blog_trash'
  ),
]
