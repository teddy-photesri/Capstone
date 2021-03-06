from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django import forms
from .models import Emotion, JournalEntry, User
import requests


def register(request):
    return render(request, 'itoneapp/register.html', {'title': 'register'})

def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    profile_image = request.FILES.get('profile_image', None)

    user = User.objects.create_user(username, email, password)
    user.profile_image = profile_image
    user.save()

    login(request, user)

    return HttpResponseRedirect(reverse('itoneapp:home'))


def login_page(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    context = {
        'next': next,
        'message': message
    }
    return render(request, 'itoneapp/login.html', context)


def login_user(request):

    next = request.POST['next']

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next != '':
            return HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse('itoneapp:home'))
    if next == '':
        return HttpResponseRedirect(reverse('itoneapp:login') + '?message=failure')
    return HttpResponseRedirect(reverse('itoneapp:login') + '?message=failure&next='+next)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('itoneapp:login') + '?message=loggedout')

@login_required
def home(request):
    # get emotions out of database
    emotions = Emotion.objects.all()
    journal_entries = JournalEntry.objects.all()

    # pass them into the data context to be rendered
    context = {
        'title': 'home',
        'emotions': emotions,
        'journal_entries': journal_entries
    }
    return render(request, 'itoneapp/home.html', context)

@login_required
def profile(request):
    context = {
        'title': 'profile',
    }
    return render(request, 'itoneapp/profile.html', context)

@login_required
def profile_edit(request, user_id=0):
    profiles = User.objects.get(id=user_id)
    context = {
        'profiles': profiles
    }
    return render(request, 'itoneapp/profile_edit.html', context)

@login_required
def profile_edit_save(request, user_id=0):
    profiles = User.objects.get(id=user_id)

    profile_image = request.FILES.get('profile_image', False)
    print(request.POST)
    username = request.POST['username']
    email = request.POST['email']

    profiles.username=username
    profiles.email=email
    if profile_image:
        profiles.profile_image=profile_image

    profiles.save()

    return HttpResponseRedirect(reverse('itoneapp:profile'))



@login_required
def journal_entry(request):
    # get emotions out of database
    emotions = Emotion.objects.all()
    selected_emotion_id = int(request.GET.get('emotion', 1))
    selected_emotion = Emotion.objects.get(id=selected_emotion_id)
    # selected_emotion = Emotion.objects.get()
    context = {
        'title': 'Journal',
        'emotions': emotions,
        'selected_emotion': selected_emotion,
    }
    return render(request, 'itoneapp/journal_entry.html', context)

@login_required
def savejournal(request):
    print(request.POST)

    # get data out of journal_entry
    intensity = request.POST['intensity']
    input_detail = request.POST['input_detail']
    name = request.POST['emotion']
    print(name)
    emotion = Emotion.objects.get(name=name)
    user = request.user

    journal_detail = JournalEntry(emotion=emotion, intensity=intensity, content=input_detail, user=user)

    # save the instance
    journal_detail.save()

    # redirect back to the journal_list view
    return HttpResponseRedirect(reverse('itoneapp:journal_list'))

@login_required
def journal_list(request):
    # get emotions out of database
    entries = JournalEntry.objects.filter(user=request.user)
    print(request.GET)
    context = {
        'title': 'List',
        'entries': entries,

    }
    return render(request, 'itoneapp/journal_list.html', context)

@login_required
def delete_journal(request, journal_detail_id=0):
    journal_detail = JournalEntry.objects.get(id=journal_detail_id)
    journal_detail.delete()

    # redirect back to the journal_list view
    return HttpResponseRedirect(reverse('itoneapp:journal_list'))

@login_required
def edit_journal(request, journal_detail_id=0):
    journal_detail = JournalEntry.objects.get(id=journal_detail_id)
    context = {
        'journal_detail': journal_detail
    }
    return render(request, 'itoneapp/journal_edit.html', context)

@login_required
def edit_save(request, journal_detail_id=0):
    journal_detail = JournalEntry.objects.get(id=journal_detail_id)

    intensity = request.POST['intensity']
    input_detail = request.POST['input_detail']
    # name = request.POST['emotion']
    # emotion = Emotion.objects.get(name=name)
    # user = request.user

    # journal_detail.emotion=emotion
    journal_detail.intensity=intensity
    journal_detail.content=input_detail
    # journal_detail.user=user

    # save the instance
    journal_detail.save()

    # redirect back to the journal_list view
    return HttpResponseRedirect(reverse('itoneapp:journal_list'))

@login_required
def evaluation(request):
    emotions = Emotion.objects.all()
    journal_entries = JournalEntry.objects.all()
    intensities = [entry.intensity for entry in journal_entries]
    intensities = str(intensities)
    # selected_emotion = JournalEntry.objects.all()

    print(request.GET)
    context = {
        'title': 'evaluation',
        'emotions': emotions,
        'journal_entries': journal_entries,
        'intensities': intensities,
        # 'selected_emotion': selected_emotion,
    }

    return render(request, 'itoneapp/evaluation.html', context)
