from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    float_field = models.FloatField("Вещественное поле")
    datetime_field = models.DateTimeField("поле временных отметок",primary_key=True)

    def __str__(self):
        return self.title
