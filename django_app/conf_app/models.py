from django.db import models

class ConferenceHall(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    date = models.DateField()
    hall = models.ForeignKey(ConferenceHall, related_name='hall', on_delete=models.CASCADE)
    description = models.TextField()
    class Meta:
        unique_together = ('date', 'hall')

    def __str__(self):
        return f'Reservation {self.id} for {self.hall}'

