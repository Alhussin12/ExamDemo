from django.urls import path
from datetime import datetime

from . import views
from django.views.decorators.csrf import csrf_exempt
fn = f'Report One Student {datetime.now()}.pdf'
urlpatterns = [
    path('ShowStudent',views.showStudent,name='ss'),
    path('AddStudent',views.addStudent,name='as'),
    path('ShowStudent/<int:pks>',views.showStudentExamCourseStatics,name='ssecs'),
    path('ShowStudent/<int:pks>/<int:ecid>',views.showStudentStaticsInOneExamCourse,name='sssinec'),
    path('postSerialVal/',csrf_exempt(views.postSerialVal),name='psv'),
    path('showStudentFilter/<int:num>',csrf_exempt(views.showStudentFilter),name='ssf'),
    path('deleteStudent/',csrf_exempt(views.deleteStudent),name='ds'),
    path('sStaFilter/<int:num>',csrf_exempt(views.sStaFilter),name='sstaf'),
    path('pdf/<int:num>',views.StudentReport,name='pdf'),
]