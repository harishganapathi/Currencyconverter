from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.ForeignKey('auth.User')
    conversion = models.CharField(max_length = 40)

    def publish(self):
        self.save()

    def __str__(self):
        return self.conversion
