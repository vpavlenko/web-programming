from django.contrib import admin
import lessons.models

admin.site.register(lessons.models.Lesson)
admin.site.register(lessons.models.Problem)
admin.site.register(lessons.models.Submission)
admin.site.register(lessons.models.Test)
