from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html' , {'form': form})
def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account opened for {username}!')
            # return redirect('blog-home')
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html' , {'form': form})

@login_required 
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm( request.POST,request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            print(u_form.cleaned_data) 
            print(p_form.cleaned_data) 
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
        else:
            messages.error(request,f"Your account has not been updated!")
        return redirect('profile')
    
            
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile) 
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return(render(request, 'users/profile.html',context)) 


