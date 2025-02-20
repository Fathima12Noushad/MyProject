from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from polls.views import welcome_view, custom_404_view #import views

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('',welcome_view, name='welcome'), #Root UR: for welcome page
    path('admin', admin.site.urls),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# Set the custom 404 error handler
handler404 = custom_404_view 