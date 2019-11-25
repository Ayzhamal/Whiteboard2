from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm, StudentUpdateForm, ProfileUpdateForm
from .models import Profile 


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
    
@login_required    
def profile(request):
    if request.method=='POST':
        # to put replaceholders in the form, we just need to pass an instance of the current user 
        # to send POST data we pass request.POST parameter
        u_form=StudentUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, 
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else: 
        u_form=StudentUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
        
    context={
        'u_form': u_form,
        'p_form':p_form
    }
    
    return render(request, 'students/profile.html', context)