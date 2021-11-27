from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=200, verbose_name='Course Name', unique=True)
    course_desc = models.CharField(max_length=200, verbose_name='Course Description', blank=True)
    course_icon = models.CharField(max_length=500, verbose_name='Course Icon', blank=True)
    created_date = models.DateTimeField('Created Date', auto_now_add=True)

    def __str__(self):
        return self.course_name

    def length_of_lessons(self):
        return len(self.lesson_set.all())
        
    
