from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coronaapp.urls')),
]





###Scraping pictures from website

# from django.contrib import admin
# from django.urls import path
# from coronaapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
# ]