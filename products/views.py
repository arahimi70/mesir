from django.views import generic
from . import models 
from . import forms
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

# Create your views here.

class ProductListView(generic.ListView):
    model = models.Product
    template_name = "home.html"


class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = "product.html"


# def Inquiry(request):
# 	form = InquiryForm(request.POST or None)
# 	context = {"form": form}
# 	template_name = "product.html"
# 	return render(request, template, context)

class InquiryCreateView(CreateView):
    form_class = forms.InquiryForm
    model = models.Inquiry
    template_name = "inquiry.html"
    context = {"form": model}
    success_url = reverse_lazy('product_list')
    # fields = ('firstname','lastname','companyname','email','description','phone')
	
