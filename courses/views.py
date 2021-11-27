from django.shortcuts import render, HttpResponse

from courses.models import Course
# Create your views here.
def index(request):
    courses = Course.objects.all()

    context = {
        'courses' : courses
    }

    return render(request, 'courses/index.html', context)


def detail(request, pk):
    course = Course.objects.filter(pk=pk)[0]
    print(course.course_name)
    

    lessons = course.lesson_set.all()
    context = {
        'course' : course,
        'lessons' : lessons,
    }

    return render(request, 'courses/detail.html', context)
        