from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^submit',views.submit,name="submit"),
    url(r'^$',views.mainpage,name="mainpage" ),
]
