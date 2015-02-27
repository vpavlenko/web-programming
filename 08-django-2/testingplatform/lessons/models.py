from django.db import models
from django.contrib.auth.models import User


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
    RE = 'RE'
    WA = 'WA'
    STATUSES = (
        (OK, 'Correct'),
        (RE, 'Run-time error'),
        (WA, 'Wrong answer'),
    )

    code = models.TextField()
    status = models.TextField(choices=STATUSES)
    problem = models.ForeignKey(Problem)
    info = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{0} (status): {1}'.format(self.problem, self.status, self.code)

    def as_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'status': self.get_status_display(),
            'info': self.info,
            'user': str(self.user),
        }
