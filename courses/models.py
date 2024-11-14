from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_all_courses():
    return Course.objects.all()

def get_course_by_id(id):
    return Course.objects.get(id=id)

def add_course(data):
    Course.objects.create(
        name = data['name'],
        desc = data['desc']
    )

def delete_course(id):
    c = Course.objects.get(id=id)
    c.delete()