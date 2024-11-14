from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses/add', views.addCourse),
    path('courses/destroy/<int:id>', views.toDeleteCourse),
    path('courses/destroy/<int:id>/delete', views.deleteCourse),
]