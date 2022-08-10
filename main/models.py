from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    float_field = models.FloatField("Вещественное поле")
    datetime_field = models.DateTimeField("поле временных отметок",primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"

class Task_2(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    float_field = models.FloatField("Рейтинг задания, где 10 - наивысший")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"

class Comment(models.Model):
    name = models.CharField("name", max_length=60)
    message = models.TextField("message")
