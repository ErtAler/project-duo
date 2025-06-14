from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator
from .models import Dish, Category
from .forms import RegisterForm



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
def dishes_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dishes/detail.html', {
        'dish': dish,
    })

def dishes_buy(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dishes/buy.html', {'dish': dish})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('index')
        else:
            messages.error(request, "Ошибка регистрации. Проверьте форму.")
    else:
        form = RegisterForm()
    return render(request, 'dishes/register.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm
    return render(request, 'dishes/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'dishes/profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')


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
