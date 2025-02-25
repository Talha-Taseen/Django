from django.shortcuts import render
from .models import MembershipPlan, Member

def membership_plans(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'membership/plans.html', {'plans': plans})

def user_membership(request):
    member = Member.objects.get(user=request.user)
    return render(request, 'membership/user_membership.html', {'member': member})
