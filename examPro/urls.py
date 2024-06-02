
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('NewExamCourseTable',views.proExam,name='examt'),
    path('ExamCourseTable',views.examTable,name='et'),
    path('ExamCourseTable/ShowExamProgram/<int:num>',views.examApi,name='eapi'),#showexamprogram
    path('ExamCourseTable/CreateTable/<int:num>',views.examProgramCreate,name='epc'),
    path('ExamCourseTable/ShowExamProgram/sss/',csrf_exempt(views.sss),name='sss'),
    path('ExamCourseTable/ShowExamProgram/pdf/<int:num>',views.examProgramReport,name='epr'),

]