from multiprocessing import context
from django.shortcuts import render
from .forms import RegistrationForm, UserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.shortcuts import render, redirect
# Create your views here.

def register(request):
    form=RegistrationForm(request.POST or None)


    if form.is_valid():
        form.save()
        return redirect("login")
    context = {
        "form":form,
    }
    return render(request,"users/register.html", context)

def profile(request):
    u_form = UserUpdateForm(request="POST" or None, instance=request.user)
    