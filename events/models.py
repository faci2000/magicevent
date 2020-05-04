from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails')
    
    def __str__(self):
        return self.title


    

class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name+" "+self.surname
