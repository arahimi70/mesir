# Create your views here.

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import *
from blog.forms import  CommentForm

from django.views import generic
from . import models


# def view_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.post = post
#         comment.save()
#         return redirect(request.path)
#     return render_to_response('blog/post.html',
#                               {
#                                   'post': post,
#                                   'form': form,
#                               },
#                               context_instance=RequestContext(request))


# def index(request, slug):
#     posts = get_object_or_404(Post, slug=slug)
#     return render(request,'templates/blog',{'posts': posts})



class BlogIndex(generic.ListView):
    queryset = models.Post.objects.published()
    template_name = 'blog.html'
    paginate_by = 2
    
class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = 'post.html'



# def index(request):
#     posts = get_object_or_404(Post)
#     return render(request,'templates/blog',{'posts': posts})