from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    re_path('blog/', include('blog.urls')),
    re_path('about/', include('about.urls')),
]
