from django.shortcuts import render
from .models import FitnessClass

def class_list(request):
    classes = FitnessClass.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})
