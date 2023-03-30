from django.db import models


class Inquirer(models.Model):
    title = models.CharField(max_length=200)
    time = models.IntegerField(default=10)

    def __str__(self):
        return self.title
