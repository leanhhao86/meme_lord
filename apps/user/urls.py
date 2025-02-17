from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='user_login'),
    path('register/', views.RegisterView.as_view(), name='user_register'),
    url(r'^profile/(?P<username>[-\w]+)/$', views.UserProfileDetailView.as_view(), name="user_profile"),
    url(r'^update/(?P<username>[-\w]+)/$', views.UserProfileUpdateView.as_view(), name="user_update"),
]