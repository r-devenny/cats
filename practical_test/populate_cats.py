# Import necessary modules
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_test.settings')
import django
django.setup()
from cats.models import Student, Cat

# Define the population function
def populate():
    # Sample data for students
    students_data = [
        {'first_name': 'Alyssa', 'last_name': 'Croft', 'cats': 3},
        {'first_name': 'John', 'last_name': 'Doe', 'cats': 1},
        {'first_name': 'Azam', 'last_name': 'Khan', 'cats': 2},
    ]

    # Populate students
    for data in students_data:
        student = Student.objects.get_or_create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            cats=data['cats']
        )[0]
        student.save()

    # Sample data for cats
    cats_data = [
        {'name': 'Alex', 'student': 'Alyssa Croft'},
        {'name': 'Luna', 'student': 'Alyssa Croft'},
        {'name': 'Mittens', 'student': 'Alyssa Croft'},
        {'name': 'Muffins', 'student': 'John Doe'},
        {'name': 'Jill', 'student': 'Azam Khan'},
        {'name': 'Joe', 'student': 'Azam Khan'},
    ]

    # Populate cats
    for data in cats_data:
        student = Student.objects.get(first_name=data['student'].split()[0], last_name=data['student'].split()[1])
        cat = Cat.objects.get_or_create(name=data['name'], student=student)[0]
        cat.save()

# Entry point to the script
if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population completed!')
