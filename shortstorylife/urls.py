from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.mainpage,name="mainpage" ),
    url(r'^story/submit/',views.submit,name="submit"),
]
