from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse

class PostQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
    

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = RichTextField()
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	meta_description = models.CharField('Meta description for SEO', max_length=155)#description for SEO purposes
	keywords = models.CharField(max_length=100, blank=True)

	objects = PostQuerySet.as_manager()
	class Meta:
		verbose_name = "Post"
		verbose_name_plural = "Posts"
		ordering = ['created']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={"slug": self.slug})

	# def get_absolute_url(self):
		# return "/blog/%s/%s/" % (self.created.year, self.slug)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

