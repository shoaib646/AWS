from django.db import models



class contact(models.Model):

    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.EmailField()
    goal = models.CharField(max_length=500)
    availability  = models.TextField(max_length=10000, )

    def __str__(self):
        return self.name