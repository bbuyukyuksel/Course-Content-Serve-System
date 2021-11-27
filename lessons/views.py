from django.shortcuts import render

from lessons.models import Lesson
# Create your views here.
def lesson(request, pk):
    lesson = Lesson.objects.filter(pk=pk)[0]

    context = {
        'lesson' : lesson,
    }

    return render(request, 'lessons/lesson.html', context)