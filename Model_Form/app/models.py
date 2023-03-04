from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name