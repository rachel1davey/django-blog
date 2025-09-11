from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog_index, name='blog_index'),
]
