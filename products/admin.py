from django.contrib import admin
from products.models import Product, Inquiry

# Register your models here.




class ProductAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product,ProductAdmin)

class InquiryAdmin(admin.ModelAdmin):

	list_display = ('created','companyname','phone','lastname','firstname',)
	list_filter = ('created','lastname')
		

admin.site.register(Inquiry,InquiryAdmin)