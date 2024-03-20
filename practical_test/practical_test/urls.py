from django.contrib import admin
from django.urls import path

from cats import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats/', views.index, name='index'),
    path('cats/about/' , views.about, name='about'),
]
