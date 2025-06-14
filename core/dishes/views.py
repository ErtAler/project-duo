from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Dish, Category


from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

def get_index(request, category_slug=None):
    categories = Category.objects.all()
    category = None

    dishes = Dish.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        dishes = dishes.filter(category=category)

    paginator = Paginator(dishes, 3)  # например, по 6 блюд на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'dishes/index.html', context)



def get_about(request):
    return render(request, 'dishes/about.html')

def get_contact(request):
    return render(request, 'dishes/contact.html')

@login_required
def dishes_detail(request, ticket_id):
    dishes = get_object_or_404(Dish, id=ticket_id)
    return render(request, 'dishes/index.html', {
        'dishes': dishes,
    })


def dishes_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    dishes = Dish.objects.filter(category=category)

    categories = Category.objects.all()

    context = {
        'category': category,
        'dishes': dishes,
        'categories': categories,
    }
    return render(request, 'dishes/index.html', context)
