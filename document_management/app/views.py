
# Create your views here.

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from datetime import datetime

from django.views import View
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from app.models import Document, Profile
from app.forms import DocumentForm, ProfileForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listDocument')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listProfile')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {
        'form': form
    })


def listProfile(request):
	if request.method == 'GET':
		form = ProfileForm(request.GET)
        profile_qs = Profile.objects.all()
        print ("print all profile_qs",profile_qs)

        return render(request, 'listProfile.html', {'profile_qs': profile_qs,})

def update(request):
    if request.method == 'GET':
        pid = request.GET.get('pid')
        print('id', pid)
        # form = ProfileForm(request.GET)
        profile_qs = Profile.objects.filter(id=pid)
        print('profile_qs', profile_qs)
        
        return render(request, 'updateprofile.html', {'profile_qs': profile_qs,})

    if request.method == 'POST':
        pid = request.GET.get('pid')
        email = request.POST.get('email')
        name = request.POST.get('name')
        dob = request.POST.get('dob')

        profile_qs = Profile.objects.filter(
                    id__iexact=pid
                    ).update(
                    email=email,
                    name=name,
                    dob=dob
                    )

        return redirect('listProfile')


def listDocument(request):
	if request.method == 'GET':
		form = DocumentForm(request.GET)
        document_qs = Document.objects.all()
        print ("print all document_qs",document_qs)

        return render(request, 'listDocument.html', {'document_qs': document_qs,})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


def deleteDocument(request, id):
    if request.method == 'GET':
        docx_qs = Document.objects.filter(id__iexact=id).delete()
        return redirect('listDocument')
        