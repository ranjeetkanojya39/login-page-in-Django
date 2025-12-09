'''from django.urls import path
from .views import index
from .import views

'''






from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Homepage
    path("contact/", views.contact, name="contact"),
    path("login/", views.login_page, name="login"),
    path("login/submit/", views.login_submit, name="login_submit"),
    path("submit/", views.submit, name="submit"),
]
