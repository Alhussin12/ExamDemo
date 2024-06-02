from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ExamCourse)
admin.site.register(models.ExamProgram)
admin.site.register(models.Course)
admin.site.register(models.Instractor)
admin.site.register(models.InstCourse)
admin.site.register(models.courseStatus)
admin.site.register(models.Student)
admin.site.register(models.studentCourse)
admin.site.register(models.StudentsStatistics)
admin.site.register(models.CourseStatistics)
admin.site.register(models.CourseDemands)
admin.site.register(models.StudentFullReport)

# admin.site.register(models.Year_Exam)
# admin.site.register(models.Student_Course_Suc)





