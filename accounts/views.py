from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from accounts.forms import CustomUserCreationForm


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully registered')
            return redirect(reverse('register'))
    return render(request, 'accounts/register.html', {'form': form})