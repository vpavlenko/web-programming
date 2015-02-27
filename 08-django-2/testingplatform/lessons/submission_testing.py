from lessons.models import Submission


def is_correst_answer_on_test(function, test):
    output = function(*eval(test.input))
    return str(output) == test.answer


def test_submission(problem, source):
    info = ''

    try:
        sandbox = {}
        exec(source, globals(), sandbox)
        function = sandbox['action']
        if all(is_correst_answer_on_test(function=function, test=test)
               for test in problem.test_set.all()):
            status = Submission.OK
        else:
            status = Submission.WA
    except Exception as e:
        status = Submission.RE
        info = str(e)

    Submission(code=source, status=status, problem=problem, info=info).save()
