from django.urls import path
from .views import membership_plans, user_membership

urlpatterns = [
    path('plans/', membership_plans, name='membership_plans'),
    path('my-membership/', user_membership, name='user_membership'),
]
