from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=24)
    lastName = models.CharField(max_length=24)
    email = models.EmailField()
    desc = models.TextField()

    
    def __str__(self):
        return self.firstName
    