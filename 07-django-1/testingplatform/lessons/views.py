from django.shortcuts import render

from lessons.models import Lesson, Problem


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'index.html', {'lessons': lessons})


def lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson.html', {'lesson': lesson})


def problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    return render(request, 'problem.html', {'problem': problem})
