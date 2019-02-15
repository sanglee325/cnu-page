from django.shortcuts import render, get_object_or_404, redirect
from members.models import Person
# Create your views here.

def index(request):
    return redirect('member')

def member(request):
    members = Person.objects.all().order_by('student_number')
    return render(request, 'members/list.html', {'members': members})
