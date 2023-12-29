from typing import Any
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from posts_app.forms import AddPostForm, CommentForm
from posts_app.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib import messages


# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        add_post_form = AddPostForm(request.POST)
        if add_post_form.is_valid():
            add_post_form.instance.author = request.user
            add_post_form.save()
            return redirect('home')
    else:
        add_post_form = AddPostForm()
    return render(request,'add_post.html', {'form':add_post_form})


# add post class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html' # J page a data gula show korabo
    success_url = reverse_lazy('add_post') # kaj sheshe je page a return korbo
    # success_url = '/posts_app/add_post/'
    def form_valid(self, form):  # j data gula frontend a pass korbo form diye
        messages.success(self.request, "Added post Successfully")
        form.instance.author = self.request.user
        return super().form_valid(form)
    


@login_required
def edit_post(request,id):
    post = Post.objects.get(pk=id)
    edit_post_form = AddPostForm(instance=post)
    if request.method == 'POST':
        edit_post_form = AddPostForm(request.POST, instance=post)
        if edit_post_form.is_valid():
            edit_post_form.instance.author = request.user
            edit_post_form.save()
            return redirect('profile')
    return render(request,'add_post.html', {'form':edit_post_form})



# Edit/update post in class based view
@method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    





@login_required
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('profile')


# delete post using class based deleteView
@method_decorator(login_required, name='dispatch')
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')




class DetailsPost(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'


    def post(self,request, *args, **kwargs):
        comment_form = CommentForm(self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


