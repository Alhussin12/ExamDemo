from django.shortcuts import render
from examPro.models import ExamCourse,Course,studentCourse,Student,CourseStatistics
from openpyxl import load_workbook
import pandas as pd
from authn.models import ExamUser
# Create your views here.
def main(request):
    # userS = ExamUser.objects.filter(user=request.user.id)[0].role
    # print(userS)

    return render(request,'main.html')
def index(request):
    obj=ExamCourse.objects.all()
    
    obj2=Course.objects.all()

    if request.method == 'POST':
            file = request.FILES['file']
            sem =int(request.POST.get('Semineter'))
            ec =int(request.POST.get('Course'))
            if str(file).endswith('.xlsx'):
                df = pd.read_excel(file,engine='openpyxl')
            if str(file).endswith('.csv'):
                df=pd.read_csv(file)
            df['courseId']=ec
            df['examCourse']=sem
            for index, row in df.iterrows():
                if studentCourse.objects.filter(studentId=row['studentId'],courseId=row['courseId'],IsSuccessed=True).exists():
                    print('there is student already succsed')
                else:
                    my_model = studentCourse.objects.update_or_create(
                        studentId=Student.objects.filter(id=int(row['studentId']))[0],
                        courseId=Course.objects.filter(id=int(row['courseId']))[0],
                        examCourse=ExamCourse.objects.filter(id=int(row['examCourse']))[0],
                        defaults={'grad':int(row['grad'])}
                        )
                #my_model = studentCourse(st,co,ex)
                # my_model.save()
               
            # Do something with the file
            course_have_statices= list(set([ i['course'] for i in  CourseStatistics.objects.values('course')]))
            return render(request, 'index.html',{'obj':obj,'obj2':obj2,'course_have_statices':course_have_statices})
    course_have_statices= list(set([ i['course'] for i in  CourseStatistics.objects.values('course')]))
    return render(request,'index.html',{'obj':obj,'obj2':obj2,'course_have_statices':course_have_statices})
