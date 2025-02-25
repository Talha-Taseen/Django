from django.db import models
class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    capacity = models.IntegerField(default=20)
    
    def __str__(self):
        return f"{self.name} - {self.instructor} ({self.schedule})"
