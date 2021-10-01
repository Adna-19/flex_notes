from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import Account
from taggit.managers import TaggableManager

class Category(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = f"{slugify(self.title)}-{slugify(timezone.now())}"
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Categories'

class Post(models.Model):
	STATUS_CHOICES = (
		('published', 'Published'),
		('draft', 'Draft'),
	)

	author   = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='posts', null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
	title    = models.CharField(max_length=255, null=True, blank=True)
	image    = models.ImageField(upload_to='media/blog/posts/images/')
	slug     = models.SlugField(max_length=200, unique=True, null=True, blank=True)
	content  = RichTextUploadingField() 
	summary  = models.TextField()
	status   = models.CharField(max_length=10, choices=STATUS_CHOICES)
	trashed = models.BooleanField(default=False)
	claps = models.PositiveIntegerField(null=True, blank=True)
	date_created   = models.DateField(auto_now_add=True)
	date_updated   = models.DateField(auto_now=True)
	date_published = models.DateField()

	tags    = TaggableManager()

	def save(self, *args, **kwargs):
		self.slug = f"{slugify(self.title)}-{slugify(timezone.now())}"
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return f"/blog/post/{self.slug}/details"

	def __str__(self):
		return self.title
