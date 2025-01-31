from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm




def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'{username} is registered')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    

    return render(request, 'user/register.html', {'form': form})
