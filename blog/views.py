from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateResponseMixin, View, RedirectView
from django.utils.dateformat import format
from .models import Post, Category
from .forms import PostForm
from accounts.models import Account
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from taggit.models import Tag
import json

class PostListView(ListView):
  model = Post 
  context_object_name = 'posts'
  paginate_by   = 6
  template_name = 'blog/post_list.html'
  category = None
  query = None

  def dispatch(self, request, *args, **kwargs):
    if 'category_slug' in kwargs:
      self.category = Category.objects.get(slug=kwargs['category_slug'])
    return super().dispatch(request, *args, **kwargs)

  def get_queryset(self):
    qs = super().get_queryset() if not self.category else super().get_queryset().filter(category=self.category)

    if 'query' in self.request.GET:
      qs = super().get_queryset().filter(title__contains=self.request.GET['query'])
    return qs.filter(status='published', trashed=False)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['tags'] = Tag.objects.all()
    return context

class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_details.html'
  context_object_name = 'post'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    context['tags'] = Tag.objects.all()
    return context

# Blog CMS Views
class CMSPostListView(ListView):
  model = Post
  context_object_name = 'posts'
  paginate_by = 10
  template_name = 'blog/cms_home.html'

  def get_queryset(self):
    qs = super().get_queryset()
    return qs.filter(author=self.request.user, trashed=False).order_by('-date_created')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['post_form'] = PostForm
    context['trash_count'] = self.request.user.posts.filter(
        trashed=True).count()
    return context


class PostCreateView(CsrfExemptMixin, JsonRequestResponseMixin, View):
	def post(self, request, *args, **kwargs):
		data = json.loads(request.POST['post_data'])
		data['category'] = Category.objects.get(id=int(data['category']))
		form = PostForm(data, request.FILES)

		if form.is_valid() and request.method == 'POST':
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
		return self.render_json_response({'message': 'POST DATA SUBMITTED...'})


class PostUpdateView(TemplateResponseMixin, View):
	template_name = 'blog/post_edit.html'

	def get(self, request, post_slug, *args, **kwargs):
		post = request.user.posts.get(slug=post_slug)
		form = PostForm(request.POST or None, request.FILES or None, instance=post)

		return self.render_to_response({
			'form': form,
			'post': post
		})

	def post(self, request, post_slug, *args, **kwargs):
		post = request.user.posts.get(slug=post_slug)
		form = PostForm(request.POST, request.FILES, instance=post)

		if form.is_valid():
			form.save()
			return redirect('blog:cms_blog')
		return self.render_to_response({'form': form, 'post': post})

class TrashUnTrashArticle(CsrfExemptMixin, JsonRequestResponseMixin, View):
	def get(self, request, *args, **kwargs):
		post = request.user.posts.get(slug=kwargs['post_slug'])
		action = kwargs['action']

		if action == 'delete':
			post.trashed = True
		elif action == 'restore':
			post.trashed = False

		post.save()
		return self.render_json_response({
			'message': 'Moved to trash' if action == 'delete' else 'Restored from Trash',
			'post_id': post.id,
			'action': action
		})

class EmptyBlogTrashView(RedirectView):
	permanent = False
	query_string = True
	pattern_name = 'cms_blog'

	def get_redirect_url(self, *args, **kwargs):
		posts = self.request.user.posts.filter(trashed=True)
		[post.delete() for post in posts if post.author == self.request.user]
		return super().get_redirect_url(*args, **kwargs)

class TrashListView(CsrfExemptMixin, JsonRequestResponseMixin, View):
	def get(self, request, *args, **kwargs):
		trashed_posts = request.user.posts.filter(trashed=True)
		results = []

		for post in trashed_posts:
			item = {
				'id': post.id,
				'title': post.title,
				'summary': f"{post.summary[:180]}...",
				'date_created': format(post.date_created, 'M, d Y'),
				'author': request.user.username,
				'slug': post.slug,
				'image': post.image.url
			}
			results.append(item)
		return self.render_json_response(results)
