from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryListCreateViewAPIView.as_view()),

]