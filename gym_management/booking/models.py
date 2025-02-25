from django.db import models
from django.contrib.auth.models import User

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    capacity = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.name} - {self.instructor} ({self.schedule})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.fitness_class.name}"
