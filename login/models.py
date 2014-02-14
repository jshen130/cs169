from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128, blank=False, unique=True)
    password = models.CharField(max_length=128, blank=True)
    counter  = models.IntegerField()
    
    def __unicode__(self):
        return self.username
    
