from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator


def get_index(request):
    return render(request, 'dishes/index.html')

def get_about(request):
    return render(request, 'dishes/about.html')

def get_contact(request):
    return render(request, 'dishes/contact.html')
