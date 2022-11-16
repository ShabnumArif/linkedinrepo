from django.urls import path
from . import views

urlpatterns = [
    path('jquery',views.jquery1),
    path('test',views.test),
    path('join_now',views.join_now),
    path('sign_in',views.sign_in),
    path('post_job',views.post_job),
    path('get_started',views.get_started),
    path('video',views.video),
]