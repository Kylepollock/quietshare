from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

from .models import FilePost

# Two example views. Change or delete as necessary.

class QuietShareForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=30)
    expiry = forms.CharField(max_length=5)
    filename = forms.FileField(label = "Select a file")

def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

def file(request):
    if request.method == 'POST':
        upload = (request.POST['filename'])

        # Create a form instance and populate it with data from the request
        form = QuietShareForm(request.POST)

        if form.is_valid():
            filepost = FilePost.objects.create(
                username=form.cleaned_data['username'],
                text=form.cleaned_data['text'],
                expiry=form.cleaned_data['expiry'],
                filename=form.cleaned_data['filename'],
            )

            # As soon as our new user is created, we make this user be
            # instantly "logged in"
            #auth.login(request, user)
            return redirect('/')

    else:
        # if a GET we'll create a blank form
        form = QuietShareForm()

    context = {
        'form': form,
    }
    return render(request, 'pages/file.html', context)
