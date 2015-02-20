from django.db import models


class Lesson(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.TextField()
    statement = models.TextField()
    lesson = models.ForeignKey(Lesson)

    def __str__(self):
        return self.title


class Test(models.Model):
    number = models.IntegerField(unique=True)
    input = models.TextField()
    answer = models.TextField()
    problem = models.ForeignKey(Problem)

    def __str__(self):
        return '{0}: {1}'.format(self.number, self.input)


class Submission(models.Model):
    OK = 'OK'
    ERROR = 'Error'
    STATUSES = (
        (OK, OK),
        (ERROR, ERROR),
    )

    code = models.TextField()
    status = models.TextField(choices=STATUSES)
    problem = models.ForeignKey(Problem)

    def __str__(self):
        return '{0} (status): {1}'.format(self.problem, self.status, self.code)
