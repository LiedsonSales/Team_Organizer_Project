from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'Team_Organizer/pages/home.html', context={
        'name':'liedson'
    })
