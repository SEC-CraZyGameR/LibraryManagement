from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import (UserRegisterForm,
                    UserProfileForm,
                    UserUpdateForm,
                    ProfileUpdateForm,
                    )
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request,f'Accout created for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    return render(request,'users/register.html',{'form':form,'profile_form':profile_form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, instance = request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.userprofile)

    context = {'u_form':u_form,'p_form':p_form}
    messages.success(request,f'Successfully Updated')
    return render(request,'users/profile.html',context)