from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

# Create your models here.


class Product(models.Model):
	"""docstring for Product"""
	name = models.CharField(max_length=100, unique=True)
	description = RichTextField()
	slug = models.SlugField(max_length=100, unique=True)


	def __str__(self):
		return self.name

	# @models.permalink
	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"slug": self.slug})


class SubProduct(models.Model):
	"""docstring for SubProduct"""
	name = models.CharField(max_length=100, unique=True)
	description = RichTextField()
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("subproduct_detail", kwargs={"name": self.name})
		
class Inquiry(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	companyname = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	description = models.TextField()
	phone = models.CharField(max_length=15)
	created = models.DateTimeField(auto_now_add=True)
	# helper = FormHelper()
	# helper.layout = Layout(
	# 	Div(
	# 		Div('field1', css_class='col-sm-5 col-sm-offset-1'),
	# 		Div('field3', css_class='col-sm-5'),  
	# 	css_class='row-fluid'), 
	# 	)

	# def __str__(self):
	# 	return self.lastname

	# def get_absolute_url(self):
	# 	return reverse('inquiry', kwargs={'created': self.created})
