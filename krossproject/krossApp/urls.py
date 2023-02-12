from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
]