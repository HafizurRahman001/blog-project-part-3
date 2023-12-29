from typing import Any
from django.shortcuts import render,redirect
from posts_app.models import Post
from author_app.forms import RegisterForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy


# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = AuthorForm(request.POST)
#         if author_form.is_valid():
#             print(author_form.cleaned_data)
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = AuthorForm()
#     return render(request,'add_author.html', {'form':author_form})




def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            messages.success(request, "Account created successfully")
            return redirect('register')
    else:
        register_form = RegisterForm()
    return render(request,'registerform.html', {'form':register_form, 'type': 'Register'})



def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            userName = login_form.cleaned_data['username']
            userPass = login_form.cleaned_data['password']
            user = authenticate(username=userName,password=userPass)
            if user is not None:
                login(request,user)
                messages.success(request, "Loged in successfully")
                return redirect('profile')
            else:
                messages.warning(request, "Login information successfully")
                return redirect('register')
    else:
        login_form = AuthenticationForm()
    return render(request,'registerform.html', {'form':login_form, 'type':'Login'})



# login using class based loginview
class UserLogIn(LoginView):
    template_name = 'registerform.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "User Loged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, "User Loged in information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    


@login_required
def update_profile(request):
        if request.method == 'POST':
            profile_form = ChangeUserData(request.POST, instance=request.user)
            if profile_form.is_valid():
                print(profile_form.cleaned_data)
                profile_form.save()
                messages.success(request, "Profile updated successfully")
                return redirect('register')
        else:
            profile_form = ChangeUserData(instance=request.user)
        return render(request,'update_profile.html', {'form':profile_form, 'type': 'Update profile'})

@login_required
def profile(request):
    postData = Post.objects.filter(author = request.user)
    return render(request,'profile.html', {'postData':postData})



@login_required
def password_change(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, data = request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            update_session_auth_hash(request,password_change_form.user)
            messages.success(request, "Password updated successfully")
            return redirect('profile')
    else:
        password_change_form = PasswordChangeForm(user=request.user)
    return render(request,'password_change.html', {'form':password_change_form, 'type': 'Password-change'})



def user_logout(request):
    logout(request)
    messages.success(request, "User Loged out successfully")
    return redirect('user_login')


