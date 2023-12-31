from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.task
