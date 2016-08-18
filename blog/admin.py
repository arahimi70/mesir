from django.contrib import admin
from blog.models import Post





class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''


#     fieldsets = [
#     ('Title',               {'fields': ['title']}),
#     ('Description',			{'fields':['meta_description']}),
#     ('Keywords', 			{'fields':['keywords']}),
#     # ('Created on',		 	{'fields': ['created']}),
#     # ('Modified on',		 	{'fields': ['modified']}),
#     ('Slug',				{'fields': ['slug']}),
#     ('Publish',				{'fields': ['publish']}),
#     ('Content',     		{'fields': ['body']}),
# ]
    list_display = ('title','created','publish')
    list_filter = ('created',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)