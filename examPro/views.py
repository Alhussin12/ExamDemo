from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import ExamCourse,ExamProgram,CourseStatistics,Course,studentCourse
from django.utils import timezone
from datetime import datetime
from django.contrib import messages as ms
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.conf import settings
from django.core.mail import send_mail
# from django.db.models import Avg, Max, Min, Count
from student.utils import render_to_pdf
from authn.models import ExamUser 

# Create your views here.

def proExam(request):
    progress =True if ExamCourse.objects.filter(inProgress=True).count()  else False
    # ExamCourseCount = all.count()
    userS = ExamUser.objects.filter(user=request.user.id)[0].role

    if request.method == 'GET':
        if 'Semester' and 'datefrom' and 'dateto' in request.GET:
            sem = request.GET.get('Semester')
            DateDrom = request.GET.get('datefrom')
            DateTO = request.GET.get('dateto')
            print(sem ,DateDrom ,DateTO)
            if sem and DateDrom and DateTO:
                if  int(sem) in [1,2,3]:
                    sepFrom= DateDrom.split('-')
                    sepTo=DateTO.split('-')
                    if int(sepFrom[1])<int(sepTo[1]) and int(sepTo[1])-int(sepFrom[1])>=1:
                        semInt=int(sem)
                        reFormatDateFrom = datetime.strptime(DateDrom,'%Y-%m-%d')
                        reFormatDateTo = datetime.strptime(DateTO,'%Y-%m-%d')
                        aware1 = timezone.make_aware(reFormatDateFrom, timezone.get_current_timezone())
                        aware2 = timezone.make_aware(reFormatDateTo, timezone.get_current_timezone())
                        if ExamCourse.objects.filter(start_date__year=sepFrom[0],Semineter=int(sem)).count() == 0:
                            newSemester=ExamCourse(Semineter=semInt,start_date=aware1,end_date=aware2,inProgress=True)
                            newSemester.save()
                            return redirect('et')
                        else:
                            ms.info(request,'there is an exam corse alredy exsist')
                    else:
                        ms.info(request,'error in date durations')
                else:
                    ms.info(request,'You entered an illogical Semester')
                    pass#  You entered an illogical Semester
            else:
                ms.info(request,'there is null values')
        else:
            pass
            # ms.info(request,'dont play with name values')
    else:
        return render(request,'multiFourm.html',{'progress':progress,'userS':userS})

    return render(request,'multiFourm.html',{'progress':progress,'userS':userS})

def examTable(request):
    # GRAD_COURSE=studentCourse.objects.filter(courseId__name='programming (1)')
    # temp=[ i.grad for i in GRAD_COURSE]
    # temp.sort()
    # occurrence = {item: temp.count(item) for item in temp}
    all  = ExamCourse.objects.all()
    ExamCourseCount = all.count()
    userS = ExamUser.objects.filter(user=request.user.id)[0].role
    def inProgress():
            for i in all :
                if True == i.inProgress:
                    return True
                else:
                    return False

    return render(request,'showTable.html', {'all':all,'progress':inProgress(),'count':ExamCourseCount,'userS':userS})

def examApi(request,num):
    # Refrash models
    for i in CourseStatistics.objects.filter(ec=num):
        i.save()
    for i in ExamProgram.objects.filter(ec=num):
        i.save()
    ec = ExamCourse.objects.get(id=num)
    c=ExamProgram.objects.filter(ec=num).all().order_by('date')
    duration = f' {ec.start_date.year}({ec.Semineter}) : {ec.start_date.month}/{ec.start_date.day} --> {ec.end_date.month}/{ec.end_date.day} :Days {c.filter(ec=num).count()}'
    paginator=Paginator(c,5)
    page=request.GET.get('page')
    try:
        c=paginator.page(page)
    except PageNotAnInteger:
        c=paginator.page(1)
    except EmptyPage:
        c=paginator.page(paginator.num_page)
    b= CourseStatistics.objects.filter(ec=num)
    Courses = Course.objects.filter()

    allcs =CourseStatistics.objects.all()
    submited = allcs.filter(ec=num,is_submited=True).count()
    corrected = allcs.filter(ec=num,is_corrected=True).count()
    allCoursesInExamProgram = allcs.filter(ec=num).count()
    submitedProg = f'{(submited/allCoursesInExamProgram)*100:.2f}'
    correctedProg = f'{(corrected/allCoursesInExamProgram)*100:.2f}'

    stat={
        'submited':submited,
        'corrected':corrected,
        'allCoursesInExamProgram':allCoursesInExamProgram,
        'submitedProg':submitedProg,
        'correctedProg':correctedProg,
        'auto':Course.objects.filter(type='Automated').count(),
        'written':Course.objects.all().count() - Course.objects.filter(type='Automated').count(), 
        'now':datetime.now().date(),
    }


    if request.method == 'GET' and 'email' in request.GET :

            
            allcs =CourseStatistics.objects.all()
            strr = ''
            strr2 = ''
            
            for i in allcs.filter(ec=num):
                if i.is_corrected:
                    strr = strr + f'<li>{i.course.name} + {i.success_rate}</li>'
                if i.is_submited:
                    strr2 = strr2 + f'<li>{i.course.name} </li>'

            allcs.filter(ec=num)
            subject = f'Report about ExamProgram  : {datetime.now().date()}'
            message = f'''<div>
                                <div style="background-color: #19376D; color: black; height:40px; color:white; text-align: center; font-size:large;" >
                                    <a style="color: white; text-derction:none;" href="http://127.0.0.1:8000/">Al-Baath University Examination Department</a>
                                </div>
                                <div style='height='500px'>
                                <h5>Progress until {datetime.now().date()}</h5>
                                <ul>
                                    <li>Courses submited : {submited}/{allCoursesInExamProgram}</li>
                                    <li>Courses corrected : {corrected}/{allCoursesInExamProgram}</li>
                                    <li>Corrected Progress: {correctedProg} </li>
                                    <li>Progress: {submitedProg} </li>
                                </ul>

                                <h5>Corrcted Courses</h5>
                                <ul>
                                    {strr}
                                </ul>

                                <h5>Submited Courses</h5>
                                <ul>
                                    {strr2}
                                </ul>
                                </div>
                                <div style="background-color: #19376D; height:40px;">.</div>
                            </div>'''
            email_from =  settings.EMAIL_HOST_USER
            recipient_list = ['hosenrast@gmail.com']
            send_mail( subject, message, email_from, recipient_list ,html_message=message,fail_silently=False)
    userS = ExamUser.objects.filter(user=request.user.id)[0].role
    cc = allcs.filter(is_corrected=True,ec=num)
    paginator=Paginator(cc,5)
    pages=request.GET.get('pages')
    try:
        cc=paginator.page(pages)
    except PageNotAnInteger:
        cc=paginator.page(1)
    except EmptyPage:
        cc=paginator.page(paginator.num_page)
    return render(request,'MoadTable.html',{'c':c,'b':b,'Courses':Courses,'stat':stat,'duration':duration,'id':num,'userS':userS,'cc':cc})

def examProgramReport(request,num):
    allcs =CourseStatistics.objects.all()
    submited = allcs.filter(ec=num,is_submited=True).count()
    corrected = allcs.filter(ec=num,is_corrected=True).count()
    allCoursesInExamProgram = allcs.filter(ec=num).count()
    submitedProg = f'{(submited/allCoursesInExamProgram)*100:.2f}'
    correctedProg = f'{(corrected/allCoursesInExamProgram)*100:.2f}'
    today = allcs.filter(is_corrected=True,ec=num)
    stat={
        'submited':submited,
        'corrected':corrected,
        'allCoursesInExamProgram':allCoursesInExamProgram,
        'submitedProg':submitedProg,
        'correctedProg':correctedProg,
        'auto':Course.objects.filter(type='Automated').count(),
        'written':Course.objects.all().count() - Course.objects.filter(type='Automated').count(), 
        'now':datetime.now().date(),
    }

    c={
        'obj':get_object_or_404(ExamCourse,pk=num),
        'stat':stat,
        'today':today
    }
    pdf = render_to_pdf('ReportExamCourse.html',c)
    if pdf:
        res =HttpResponse(pdf,content_type='application/pdf')
        fn = f'Report Student  - {datetime.now().date()}'
        cont = f'inline; filename= {fn}'
        res['Content-Disposition'] = cont
        return res
    return HttpResponse('page not found')



def examProgramCreate(request,num):
    ec = ExamCourse.objects.get(id=num)
    c=ExamProgram.objects.all().order_by('date')
    b= CourseStatistics.objects.filter(ec=num)
    Courses = Course.objects.filter()
    duration = f' {ec.start_date.year}({ec.Semineter}) : {ec.start_date.month}/{ec.start_date.day} --> {ec.end_date.month}/{ec.end_date.day} :Days {c.filter(ec=num).count()}'
    
    if request.method == 'POST' and 'save' in request.POST:
        date = request.POST.get('date')
        one = request.POST.get('o')
        tow = request.POST.get('t')
        three = request.POST.get('th')
        four = request.POST.get('f')
        five = request.POST.get('fi')

        if date:
            reFormatDate = datetime.strptime(date,'%Y-%m-%d').date()
            if ec.start_date<= reFormatDate and ec.end_date.date()>=reFormatDate:
                if one == 'None' and tow =='None' and three =='None' and four == 'None' and five == 'None':
                    ms.info(request,'null courses at least one')
                else:
                    courses=[]
                    couId = [
                    one if one!='None' else '',
                    tow if tow!='None' else '',
                    three if three!='None' else '',
                    four if four!='None' else '',
                    five if five!='None' else ''
                    ]
                    couId = [eval(i) for i in couId if i ]
                    for i in couId:
                        courses.append(Course.objects.get(id=i))
                    if ExamProgram.objects.values('course').count() != 0:
                        perCourse = ExamProgram.objects.filter(ec=num)[0].course.all()
                        for i in courses:
                            if i in perCourse:
                                ms.info(request,'the course is alredy added in perv date')
                                paginator=Paginator(c,5)
                                page=request.GET.get('page')
                                try:
                                    c=paginator.page(page)
                                except PageNotAnInteger:
                                    c=paginator.page(1)
                                except EmptyPage:
                                    c=paginator.page(paginator.num_page)
                                userS = ExamUser.objects.filter(user=request.user.id)[0].role
                                return render(request,'addExamProgram.html',{'c':c,'b':b,'Courses':Courses,'duration':duration,'userS':userS})
                    else:
                        perCourse=None

                    if c.filter(date=reFormatDate).exists():
                        ms.info(request,'you added this date')
                    else:
                        obj ,cre =ExamProgram.objects.update_or_create(ec=ExamCourse.objects.get(id=num),date=reFormatDate,time=datetime.now().time())
                        obj.course.set(courses)
                        obj.save()
                        ms.success(request,'row added')
            else:
                ms.info(request,'Date must be larger than start_date and smaller than end_date')
        else:
            ms.info(request,'please Enter a valid date')
        userS = ExamUser.objects.filter(user=request.user.id)[0].role
        return render(request,'addExamProgram.html',{'c':c,'b':b,'Courses':Courses,'duration':duration,'userS':userS})
    if request.method == 'POST' and 'delete' in request.POST:
        ep  = c.filter(id=int(request.POST.get('delete'))).delete()
        ms.success(request,'delete row')


    
    paginator=Paginator(c,5)
    page=request.GET.get('page')
    try:
        c=paginator.page(page)
    except PageNotAnInteger:
        c=paginator.page(1)
    except EmptyPage:
        c=paginator.page(paginator.num_page)
    userS = ExamUser.objects.filter(user=request.user.id)[0].role
    sds= CourseStatistics.objects.filter(ec=num,course__year__in=['1','2']).order_by('course__year')
    if request.method == 'GET' and 'sss' in request.GET:
        CoSc = request.GET.get('CoSc')
        QSs = request.GET.get('QS')

        if CoSc == 'on':
            
            CoSc = True
        else:
            CoSc = False
        if QSs == 'on':
            QSs =True
        else:
            QSs = False         
        CourseStatistics.objects.filter(ec=num,id=int(request.GET.get('sss'))).update(is_Correcten_Scale_submited=CoSc,is_Question_submited=QSs)
    if request.method == 'GET' and 'corS' in request.GET:
        sdsadsd = CourseStatistics.objects.filter(ec=num,id=int( request.GET.get('corS')))[0]
        if not sdsadsd.is_Correcten_Scale_submited:
            subject = f'Report about Correction Scale  : {datetime.now().date()}'
            message = f'''<div>
                                <div style="background-color: #19376D; color: black; height:40px; color:white; text-align: center; font-size:large;" >
                                    <a style="color: white; text-derction:none;" href="http://127.0.0.1:8000/">Al-Baath University Examination Department</a>
                                </div>
                                <div style='height='500px'>
                                  {sdsadsd.course.name} مرحبا دكتور رجاءا ارسل سلم المادة
                                </div>
                                <div style="background-color: #19376D; height:40px;">.</div>
                            </div>'''
            email_from =  settings.EMAIL_HOST_USER
            recipient_list = ['hosenrast@gmail.com']
            send_mail( subject, message, email_from, recipient_list ,html_message=message,fail_silently=False)
            ms.success(request,'send email success')
        
        else:
            ms.info(request,'this Course alreay resived')
    if request.method == 'GET' and 'qsb' in request.GET:
        sdsadsd = CourseStatistics.objects.filter(ec=num,id=int( request.GET.get('qsb')))[0]

        if not sdsadsd.is_Question_submited:
            subject = f'Report about question  : {datetime.now().date()}'
            message = f'''<div>
                                <div style="background-color: #19376D; color: black; height:40px; color:white; text-align: center; font-size:large;" >
                                    <a style="color: white; text-derction:none;" href="http://127.0.0.1:8000/">Al-Baath University Examination Department</a>
                                </div>
                                <div style='height='500px'>
                                  {sdsadsd.course.name}الرجاء ارسال الاسئلة ان وقت الامتحان قريب للمادة 
                                </div>
                                <div style="background-color: #19376D; height:40px;">.</div>
                            </div>'''
            email_from =  settings.EMAIL_HOST_USER
            recipient_list = ['hosenrast@gmail.com']
            send_mail( subject, message, email_from, recipient_list ,html_message=message,fail_silently=False)
            ms.success(request,'send email success')
        else:
            ms.info(request,'this course already reseved his qustions')
    
    

        
    return render(request,'addExamProgram.html',{'sds':sds,'c':c,'b':b,'Courses':Courses,'duration':duration,'userS':userS})

import json
from django.http import JsonResponse
def sss(request):

    data=json.loads(request.body)
    id= data['id']
    ch=data['ch']

    # for i in objs:
    #         item={
    #             'id':i.pk,
    #             'firstName':i.firstName,
    #             'lastName':i.lastName,
    #             'year':i.academic_year,
    #         }
    #         data.append(item)


    return JsonResponse({'s':'Done'})

#student statistc