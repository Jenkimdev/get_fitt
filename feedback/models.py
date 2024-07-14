from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    rating = models.IntegerField(default=0)  
    message = models.TextField()
    