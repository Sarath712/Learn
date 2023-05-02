from django.db import models
app_name = 'carapp'


# Create your models here.
class Task(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name