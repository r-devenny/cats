from django.shortcuts import render
from cats.models import Student, Cat

# Create your views here.

def index(request):
    student_list = Student.objects.order_by('last_name').all()
    cats_list = Cat.objects.order_by('name').all()

    context_dict = {}
    context_dict['students'] = student_list
    context_dict['cats'] = cats_list
    return render(request, 'cats/index.html', context=context_dict)

def about(request):
    cats_list = Cat.objects.order_by('name').all()

    context_dict = {}
    context_dict['cats'] = cats_list
    return render(request, 'cats/about.html', context=context_dict)
