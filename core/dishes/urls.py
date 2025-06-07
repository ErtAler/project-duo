from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.get_index, name='index'),
    path('about/', views.get_about, name='about'),
    path('contact/', views.get_contact, name='contact')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)