from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  #here we create object of the form and pass the data to it 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html' , {'form': form})# here we are passing a dictionary named form to the template which contains the form object.
                                                                    #The template will use this form object to render the form in HTML.
# here the render function takes three arguments:request, template name and context. context is a dictionary that contains the data that will be passed to the template.

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

@login_required #decorator to ensure that only logged in users can access this view
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
#form to update username and email, here request.post and files are used to send data to the server
        p_form= ProfileUpdateForm( request.POST,request.FILES,instance= request.user.profile)#form to update image
        if u_form.is_valid() and p_form.is_valid(): #if both forms are valid
            print(u_form.cleaned_data) #cleaned data is the data that is validated and cleaned by the form
            print(p_form.cleaned_data) #cleaned data is the data that is validated and cleaned by the form
            u_form.save()# request. sends data to the server(middleman(django) that handles user request , runs code , and talk to the database) but .save() saves the data to the database(storage system that holds all the data)
            p_form.save()
            messages.success(request, f'Your account has been updated!')
        else:
            messages.error(request,f"Your account has not been updated!")
        return redirect('profile')
    
            
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile) # here instance  loads the current profile data into the form so that it can be edited
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return(render(request, 'users/profile.html',context)) #rendering means mixing template + context(here that is ofrm ) and produces a full html to show in browser


