from django.db import models
from courses.models import Course

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=200, verbose_name='Lesson Name')
    lesson_desc = models.CharField(max_length=500, verbose_name='Lesson Description', blank=True)
    video_path = models.CharField(max_length=500, verbose_name='Video Path', blank=True)
    content_path = models.CharField(max_length=500, verbose_name='Content Path', blank=True)
    is_watched = models.BooleanField(verbose_name='is watched?', default=False)

    def __str__(self):
        return f"{self.course.course_name} : {self.lesson_name}"