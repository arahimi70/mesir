from django.conf.urls import patterns, url, include
from . import views

urlpatterns = [
	url(r'^$', views.ProductListView.as_view(), name='product_list'),
	url(r'^(?P<slug>\S+)$', views.ProductDetailView.as_view(), name='product_detail'),
	url(r'^inquiry$',views.InquiryCreateView.as_view(),name='inquiry')
]