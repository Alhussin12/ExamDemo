from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('',views.course,name='course'),
    path('statistic',views.statistic,name='statistic'),
    path('addCourse',views.addCourse,name='addCourse'),
    path('addGrade',views.addGrade,name='addGrade'),
    path("yearCourseJson/",csrf_exempt(views.yearCourseJson), name='ycj'),
    path('addCourseJson/',csrf_exempt(views.addCourseJson),name='acj'),
    path('searchCourseJson/<int:num>',csrf_exempt(views.searchCourseJson),name='scj')
]