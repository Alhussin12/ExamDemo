from django.shortcuts import render
from examPro.models import ExamCourse,Course,studentCourse,Student,CourseStatistics
import pandas as pd
from django.http import JsonResponse
from examPro.models import Course ,Instractor
import json
from django.contrib import messages as ms
from authn.models import ExamUser
# Create your views here.
def addGrade(request):
    obj=ExamCourse.objects.all()
    if request.method == 'POST':
        file = request.FILES['file']
        sem =int(request.POST.get('Semineter'))
        ec =int(request.POST.get('Course'))
        year =int(request.POST.get('year'))
        if CourseStatistics.objects.filter(ec=sem,course=ec).count() !=0:
           if CourseStatistics.objects.filter(ec=sem,course=ec)[0].is_submited:
            if CourseStatistics.objects.filter(ec=sem,course=ec)[0].is_Correcten_Scale_submited:
                if file and sem and ec:
                    if str(file).endswith('.xlsx') or str(file).endswith('.csv'):
                        if str(file).endswith('.xlsx'):
                            df = pd.read_excel(file,engine='openpyxl')
                        if str(file).endswith('.csv'):
                            df=pd.read_csv(file)
                        df['courseId']=ec
                        df['examCourse']=sem
                        co=0
                        up=0
                        if 'grad' not in df.columns or  'id' not in df.columns:
                            
                            for index, row in df.iterrows():
                                    my_model,cr = studentCourse.objects.update_or_create(
                                        studentId=Student.objects.filter(id=int(row['studentId']))[0],
                                        courseId=Course.objects.filter(id=int(row['courseId']))[0],
                                        examCourse=ExamCourse.objects.filter(id=int(row['examCourse']))[0],
                                        defaults={'grad':int(row['grad'])}
                                        )
                                    if cr:
                                        co=co+1
                                    else:
                                        up=up+1
                            ms.success(request,f'there is {co} created and {up} updated Or remain')
                        else:
                            ms.info(request,'check from ur fileds name')
                    else: 
                        ms.info(request,'please enter csv or xls file')
                else:
                    ms.info(request,'there is null value')
            else:
                ms.info(request,'the course didnt get Correct Scale')
           else:
            ms.info(request,'the course in not submited')
        else:
            ms.info(request,'this course are not in exam program')
    return render(request,'course/courseGrade.html',{'obj':obj})

def yearCourseJson(request):
    data =json.loads(request.body)
    year =data['year']
    years=Course.objects.filter(year=year)
    add= []
    for i in years :
        item={
            'course':i.name,
            'id':i.pk,
        }
        add.append(item)
    return JsonResponse({'s':add})

def statistic(request):
    return render(request,'course/Statistic.html')

def addCourse(request):
    all= Instractor.objects.all()
    size =Course.objects.all().count()
    # userS = ExamUser.objects.filter(user=request.user.id)[0].role
    c={
        'all':all,
        'size':size,
        # 'userS':userS
    }
    
    return render(request,'course/addCourse.html',c)

def addCourseJson(request):
    data =json.loads(request.body)
    year =data['year']
    dept= data['dept']
    cn =data['courseName']
    type = data['type']
    inst =data['inst']
    if year and dept and cn and type:
        if type == 'None'  or year == 'None' :
            return JsonResponse({'e':'there is None Value'})
        else:
            if cn in  [i.name for i in Course.objects.filter(name=cn)]:
                return JsonResponse({'e':'already u added this course'})
            else:
                z = [inst]
                a = Course.objects.create(name=cn,type=type,year=year,dept=dept)
                a.instractor.set(z)
                a.save()
                return JsonResponse({'s':"Course Added"})
    else:
        return JsonResponse({'e':"There is null value"})

def searchCourseJson(request,num):
    ves=5
    upper = num
    lower = upper-ves
    data =json.loads(request.body)
    year =data['year']
    dept= data['dept']
    cn =data['courseName']
    type = data['type']
    inst =data['inst']
    if not year or year =='None':
        year=''
        
    if not cn:
        cn=''
    if not type or type=='None':
        type=''
    if not dept or dept =='None':
     z = Course.objects.filter(name__icontains=cn,year__icontains=year,type__icontains=type)
    else :
     dept='None'
     z = Course.objects.filter(name__icontains=cn,year__icontains=year,type__icontains=type,dept=dept)

    lists=[]
    for i in z:
        item={
            'year':i.year,
            'dept':i.dept,
            'cn':i.name,
            'type':i.type,
            'id':i.pk,
        }
        lists.append(item)

    return JsonResponse({'s':lists[lower:upper],'size':len(lists)})
