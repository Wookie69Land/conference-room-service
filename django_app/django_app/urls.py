"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from conf_app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('halls/', v.show_halls, name='halls'),
    path('room/new', v.add_hall, name='add_hall'),
    path('halls_details/', v.show_halls_details, name='halls_details'),
    path('room/reserve/<int:id>', v.add_reservation, name='add_reservation'),
    path('reserve/', v.new_reservation, name='new_reservation'),
    path('room/delete/<int:id>', v.delete_hall, name='delete_hall'),
    path('room/modify/<int:id>', v.edit_hall, name='edit_hall'),
    path('reservations/', v.show_reservations, name='show_reservations'),
]
