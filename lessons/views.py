import markdown
import codecs

from django.shortcuts import render

from lessons.models import Lesson
# Create your views here.
def lesson(request, pk):
    mdcontent = None
    lesson = Lesson.objects.filter(pk=pk)[0]

    if lesson.content_path:
        with codecs.open(lesson.content_path, 'r', 'utf-8') as f:
            mdcontent = markdown.markdown(f.read(), extensions=['fenced_code', 'codehilite'])

    context = {
        'lesson' : lesson,
        'markdown' : mdcontent,
    }

    return render(request, 'lessons/lesson.html', context)