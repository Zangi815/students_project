import random
from django.shortcuts import render


def get_random_students():
    names = ["John", "Jane", "Alex", "Alice", "Michael", "Sara", "Tom", "Lilly"]
    surnames = ["Smith", "Brown", "Wilson", "Taylor", "Anderson", "Thomas", "White"]
    
    students = []
    for _ in range(100):
        student = {
            "name": random.choice(names),
            "surname": random.choice(surnames),
            "course": random.randint(1, 4)
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    student = random.choice(students)  
    context = {'student': student}
    return render(request, 'students/main_page.html', context)


def students_page_view(request):
    students = get_random_students()
    context = {'students': students}
    return render(request, 'students/students_page.html', context)
