from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from examPro.models import Student,studentCourse,ExamCourse,StudentsStatistics,StudentFullReport
from django.contrib import messages as mess
import pandas as pd
import json
from django.db.models import Avg,Count,Sum
from datetime import datetime
from .utils import render_to_pdf
# from django.core import serializers
from authn.models import ExamUser 



# Show Student
def showStudent(request):
    # userS = ExamUser.objects.filter(user=request.user.id)[0].role

    return render(request,'showStudent.html')

def deleteStudent(request):
    data=json.loads(request.body)
    id=data['studentId']
    Student.objects.filter(id=int(id)).delete()
    return JsonResponse({'s':'Delete Sucssefully'})

def showStudentFilter(request,num):
    ves = 10
    upper = num
    lower =upper - ves
    data=json.loads(request.body)
    fn= data['firstName']
    ln=data['lastName']
    yr=data['year']
    serial =data['serial']
    if not serial:
        serial ='' 
    if not ln:
        ln = ''
    if not fn:
        fn = ''
    if not yr:
        yr =''
    objs =  Student.objects.filter(
        firstName__icontains=fn,
        lastName__icontains=ln,
        academic_year__icontains=yr,
        id__icontains = serial
        )
    data =[]
    for i in objs:
            item={
                'id':i.pk,
                'firstName':i.firstName,
                'lastName':i.lastName,
                'year':i.academic_year,
            }
            data.append(item)


    return JsonResponse({'s':data[lower:upper],'size':len(data)})

#student statistc
def showStudentExamCourseStatics(request,pks):
    # Get all records that do not have an id of 1 or a name of 'John'
    # records = MyModel.objects.exclude(id=1).exclude(name='John')
    stat = studentCourse.objects.filter(studentId=pks,examCourse=ExamCourse.objects.filter(inProgress = True)[0].id)
    allstudStat =  StudentsStatistics.objects.filter(stu=pks).order_by('-ec__start_date')
    # studentOneYear =Student.objects.filter(id=pks).values('academic_year')[0]['academic_year']
    # avgStuInEachEx = StudentsStatistics.objects.filter(stu__academic_year=studentOneYear).values('ec__start_date__year','ec__Semineter').annotate(avg=Avg('average_grade'))
    studentOneYear =Student.objects.filter(id=pks).values('academic_year')[0]['academic_year']
    avgStuInEachEx = StudentsStatistics.objects.filter(stu__academic_year=studentOneYear).values('stu__academic_year','ec__start_date__year','ec__Semineter').order_by('-ec__start_date__year','-ec__Semineter').annotate(avg=Avg('average_grade'))
    # for i in avgStuInEachEx:
    avgStuInEachExAll = StudentsStatistics.objects.values('ec__start_date__year','ec__Semineter').order_by('-ec__start_date__year','-ec__Semineter').annotate(avg=Avg('average_grade'))


    avg=StudentsStatistics.objects.filter(stu=pks).aggregate(a=Avg('average_grade'))['a']
    if not avg:
        avg=0

    att= StudentsStatistics.objects.filter(stu=pks).aggregate(a=Sum('grade_count'))['a']
    if not att:
        att=0

    suc = StudentsStatistics.objects.filter(stu=pks).aggregate(a=Sum('success_grades_count'))['a']

    if not suc :
        ar=0
    else:
        ar =f"{(suc/att)*100:.2f}"

    if not suc:
        suc=0
    overAll={
        'avg': f'{avg:.2f}',
        'att':att,
        'suc' :suc,
        'fail' : att-suc,
        'ar':ar
    }
    name = Student.objects.filter(id=pks)[0].firstName+ ' ' +Student.objects.filter(id=pks)[0].lastName
    # userS = ExamUser.objects.filter(user=request.user.id)[0].role
    c={
        'obj':get_object_or_404(Student,pk=pks),
        'stat':stat,
        'allstudStat':allstudStat,
        'avgStuInEachEx':avgStuInEachEx,
        'avgStuInEachExAll':avgStuInEachExAll,
        'overAll':overAll,
        'id':pks,
        'name':name,
        # 'userS':userS
    }

    return render(request,'studentAllStatistic.html',c)

def StudentReport(request,num):
    avg=StudentsStatistics.objects.filter(stu=num).aggregate(a=Avg('average_grade'))['a']
    att= StudentsStatistics.objects.filter(stu=num).aggregate(a=Sum('grade_count'))['a']
    suc = StudentsStatistics.objects.filter(stu=num).aggregate(a=Sum('success_grades_count'))['a']
    s=str(Student.objects.filter(id=num)[0].firstName)+' _ '+str(Student.objects.filter(id=num)[0].lastName)

    c={
        'a':StudentsStatistics.objects.filter(stu__id=num),
        's':s,
        'date':datetime.now().date(),
        'avg': f'{avg:.2f}',
        'att':att,
        'suc' :suc,
        'fail' : att-suc,
        'ar':  f"{(suc/att)*100:.2f}",
        'course':studentCourse.objects.filter(studentId=num,grad__gte=60).order_by('-examCourse__start_date','-examCourse__Semineter'),
        'ex':ExamCourse.objects.all(),
        'request':request
        }

    pdf = render_to_pdf('StudentReport.html',c)
    if pdf:
        res =HttpResponse(pdf,content_type='application/pdf')
        fn = f'Report Student {s} - {datetime.now().date()}'
        cont = f'inline; filename= {fn}'
        res['Content-Disposition'] = cont
        return res
    return HttpResponse('page not found')

def showStudentStaticsInOneExamCourse(request,pks,ecid):

    grade =studentCourse.objects.filter(studentId=pks,examCourse=ecid)
    stat =StudentsStatistics.objects.filter(stu=pks,ec=ecid)[0]
    fail =stat.grade_count-stat.success_grades_count
    ar =(stat.success_grades_count/stat.grade_count)*100
    avg = f'{stat.average_grade:.2f}'

    date =StudentsStatistics.objects.filter(stu=pks,ec=ecid).values('ec__start_date__year','ec__Semineter')
    ec =str(date[0]['ec__start_date__year'] )+' - '+str(date[0]['ec__Semineter'])
    name = Student.objects.filter(id=pks)[0].firstName+ ' ' +Student.objects.filter(id=pks)[0].lastName
    userS = ExamUser.objects.filter(user=request.user.id)[0].role
    
    c={
        'grade':grade,
        'stat':stat,
        'fail':fail,
        'ec':ec,
        'avg':avg,
        'ar':f'{ar:.2f}',
        'name':name,
        'pkss':pks,
        'userS':userS

    }
    return render(request,'oneStudentStatic.html',c)


def sStaFilter(request,num):
    ves = 2
    upper = num
    lower =upper - ves
    data =json.loads(request.body)
    year = data['years']
    sem = data['sem']
    id =  data['id']
    ss=None
    if int(data['dis']) == 1:
        ss = StudentsStatistics.objects.filter(stu=id)
    else:
        if str(year).isdigit() or str(sem).isdigit():
            # if not year :
            #     year=''
            # if not sem:
            #     sem=''
            ss = StudentsStatistics.objects.filter(stu=id,ec__start_date__year__icontains=year,ec__Semineter__icontains=sem).order_by('ec__start_date__year','ec__Semineter')
        else:
            if not year and not sem:
                ss = StudentsStatistics.objects.filter(stu=id)
            else:
                return JsonResponse({'e':'pleas enter number in sem and year'})
    datas=[]
    for i in ss:
        item={
        'average_grade': i.average_grade,
        'year':i.ec.start_date.year,
        'Semineter':i.ec.Semineter,
        'success_grades_count':i.success_grades_count,
        'grade_count':i.grade_count,
        'ec':i.ec.pk,
        }
        datas.append(item)
    return JsonResponse({'s':datas[lower:upper],'size':ss.count()})

# Add student
def addStudent(request):
    if request.method == 'POST':
        year= request.POST.get('year')
        file = request.FILES['file']
        if file and year:
            if str(file).endswith('.xls'):
                df = pd.read_excel(file)
                df['academic_year']=int(year)
                created = 0
                for i,row in df.iterrows() :
                    row,cre = Student.objects.update_or_create(
                        pk = row['id'],
                        defaults={
                            'lastName':row['lastName'],
                            'firstName':str(row['firstName']),
                            'academic_year':int(row['academic_year']),
                    })
                    if cre ==True:
                        created=+1
                mess.success(request,f'Students :: Added :{created}')
            elif str(file).endswith('.csv'):
                df = pd.read_csv(file)
                df['academic_year']=int(year)
                created = 0
                for i,row in df.iterrows() :
                    row,cre = Student.objects.update_or_create(
                    pk = row['id'],
                    defaults={
                            'lastName':row['lastName'],
                            'firstName':str(row['firstName']),
                            'academic_year':int(row['academic_year']),
                    })
                    if cre ==True:
                        created=+1  
                mess.success(request,f'Students :: Added :{created}')
            else:
                mess.info(request,'That Is Not Excil or Csv File')
        else:
            mess.info(request,'You Cant Upload Without File OR Year')
    userS = ExamUser.objects.filter(user=request.user.id)[0].role
    
    return render(request,'addStudent.html',{'userS':userS})

def postSerialVal(request):
    data=json.loads(request.body)
    sn=data['SN']
    fn=data['FirstName']
    ln=data['LastName']
    yr=data['year']
    if sn and fn and ln and yr:
        if not str(sn).isdigit():
            return JsonResponse({'e':'Please Enter Number In Serial Filed'})
        else:
            ss=Student.objects.filter(id=int(sn)).count()
            if ss != 0:
                return JsonResponse({'e':'The Serial Number Already Found'})
            else:
                asd = Student(id=sn,firstName=fn,lastName=ln,academic_year=yr)
                asd.save()
                return JsonResponse({'s':'Add sucsssefully'})
    else:
        return JsonResponse({'e':'There Is Null Values'})
