from django.shortcuts import render, redirect
from courses import models

# Create your views here.
def index(request):
    context = {
        'courses'   : models.get_all_courses()
    }
    return render(request, "index.html", context)

def addCourse(request):
    models.add_course(request.POST)
    return redirect('/')

def toDeleteCourse(request, id):
    context = {
        'course' : models.get_course_by_id(id)
    }
    return render(request, "delete_course.html", context)

def deleteCourse(request, id):
    models.delete_course(id)
    return redirect('/')