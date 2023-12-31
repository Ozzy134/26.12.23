from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
