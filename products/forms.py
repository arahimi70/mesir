from django import forms 
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div




class InquiryForm(forms.ModelForm):
	class Meta:
		model = models.Inquiry
		fields = ('firstname','lastname','companyname','email','subject','description','phone')	

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(
				Div('firstname','lastname','phone','email','companyname', css_class='col-sm-5 col-sm-offset-1',),
				Div('subject','description', css_class='col-sm-5'),  
			css_class='row-fluid'), 
			
			)
		self.helper.add_input(Submit('submit','Submit')),
		super(InquiryForm, self).__init__(*args, **kwargs)



		