"""webappspy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import emaillist.views as emaillist_views
import guestbook.views as guestbook_views
import GB.views as GB_views

urlpatterns = [

    path('emaillist/', emaillist_views.index),
    path('emaillist/form', emaillist_views.form),
    path('emaillist/add', emaillist_views.add),

    path('admin/', admin.site.urls),

    path('guestbook/', guestbook_views.index),
    path('guestbook/add', guestbook_views.add),
    path('guestbook/delete', guestbook_views.delete),
    path('guestbook/deleteform', guestbook_views.deleteform),

]
