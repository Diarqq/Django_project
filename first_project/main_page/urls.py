from django.urls import path

from .views import *

urlpatterns = [
    path('',starting_main_page),
    path('all_posts/',all_posts),

]