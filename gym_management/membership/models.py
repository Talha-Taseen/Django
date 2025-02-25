from django.db import models
from django.contrib.auth.models import User

class MembershipPlan(models.Model):
    PLAN_CHOICES = [
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    ]
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=1, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_duration_display()}) - ${self.price}"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
