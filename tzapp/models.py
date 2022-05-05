from django.db import models

# Create your models here.

class Direction(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'направлении'


class Course(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, blank=True, null=True, related_name='directions')
    title = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True, related_name='courses')
    title = models.CharField(max_length=100)
    anons = models.CharField(max_length=255)
    description = models.TextField()
    upload_file = models.FileField(upload_to='uploads_file')
    upload_video = models.FileField(upload_to='uploads_video')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'уроки'


class LessonMaterial(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True, related_name='lessons')
    title = models.CharField(max_length=100)
    context1 = models.TextField()
    context2 =models.TextField()
    image = models.ImageField(upload_to='uploads_image')
    upload_file_1 = models.FileField(upload_to='uploads_file_1')



    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'материалы'



