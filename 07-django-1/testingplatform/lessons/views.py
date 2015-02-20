from django.shortcuts import redirect, render

from lessons.models import Lesson, Problem
from lessons.submission_testing import test_submission


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'index.html', {'lessons': lessons})


def lesson(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson.html', {'lesson': lesson})


def problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    tests = problem.test_set.order_by('number')
    return render(request, 'problem.html', {'problem': problem, 'tests': tests})


def send_submission(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    source = request.POST['source']
    test_submission(problem, source)
    return redirect('problem', problem_id=problem.id)
