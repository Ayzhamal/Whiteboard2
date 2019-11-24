from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegisterForm


def register(request):
    if request.method=='POST':
        form=StudentRegisterForm(request.POST)
        if form.is_valid():
            # to save a new user object 
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created for {username}. You are now able to log in!')
            return redirect('login')
    else:
        form=StudentRegisterForm()
    return render(request, 'students/register.html', {'form': form})
    
    