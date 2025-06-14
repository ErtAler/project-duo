from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('', views.get_index, name='index'),
    path('about/', views.get_about, name='about'),
    path('contact/', views.get_contact, name='contact'),
    path('<int:pk>/buy/', views.dishes_buy, name='dishes_buy'),
    path('<int:pk>/', views.dishes_detail, name='dishes_detail'),
    path('dishes/<slug:category_slug>/', views.get_index, name='dishes_by_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)