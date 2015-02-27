import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

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


@login_required
def send_submission(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    source = request.POST['source']
    test_submission(problem, source, request.user)
    return redirect('problem', problem_id=problem.id)


def load_submissions(request):
    '''
    Ajax request.

    Params:
        problem_id

    Return: {
        'submissions': ...
    }
    '''
    problem = Problem.objects.get(id=int(request.GET['problem_id']))
    submissions_json = [submission.as_dict()
                        for submission in problem.submission_set.all()]
    response_data = {
        'submissions': submissions_json
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.authenticate
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
