#%%
from django.db.models.signals import post_save,post_delete,pre_save,m2m_changed
from django.dispatch import receiver
from .models import studentCourse,StudentsStatistics,CourseStatistics,ExamProgram,Student,CourseDemands,Course
from django.db.models import Avg, Max, Min,StdDev, Variance,Sum
from django.utils import timezone
# from grade to ss u/c
@receiver(post_save, sender=studentCourse)
def calculate_statistics(sender, instance, created, **kwargs):
    # Calculate the statistics for the updated or created CourseStudent object
    grades = studentCourse.objects.filter(studentId=instance.studentId,examCourse=instance.examCourse)
    grade_count = grades.count()
    if grade_count > 0:
        success_grades_count =grades.filter(grad__gte=60).count()
        average_grade = grades.aggregate(Avg('grad'))['grad__avg']
        max_grade = grades.aggregate(Max('grad'))['grad__max']
        min_grade = grades.aggregate(Min('grad'))['grad__min']
        grade_stddev = grades.aggregate(StdDev('grad'))['grad__stddev']
        grade_variance = grades.aggregate(Variance('grad'))['grad__variance']
        # plt.hist(grade_stddev)
    else:
        success_grades_count=None
        average_grade = None
        max_grade = None
        min_grade = None
        grade_stddev = None
        grade_variance = None

    # Save the statistics in the StudentStatistics table
    StudentsStatistics.objects.update_or_create(
        stu=instance.studentId, ec=instance.examCourse,
        defaults={
        'average_grade': average_grade,
        'max_grade': max_grade,
        'min_grade': min_grade, 
        'grade_count': grade_count,
        'grade_stddev':grade_stddev,
        'grade_variance':grade_variance,
        'success_grades_count':success_grades_count
        }
    )


# m2m chang Course add
@receiver(m2m_changed, sender=ExamProgram.course.through)
def handle_exam_changes(sender, instance,action, reverse, model, pk_set, **kwargs):
        traker = ExamProgram.objects.get(date=instance.date,ec=instance.ec).tracker
        if traker:
            is_submited=True
        else: 
            is_submited =False
        if action == 'post_add':
                for i in instance.course.all():
                    if not CourseStatistics.objects.filter(course=i,ec=instance.ec).exists():
                        CourseStatistics.objects.create(course=i,ec=instance.ec,average_grade=0,max_grade=0,min_grade=0,grade_count=0,is_submited=is_submited)
        # elif action == 'post_remove':
        #     # handle exams that were removed from the course
        #     for exam_id in pk_set:
        #         exam = Exam.objects.get(id=exam_id)
        #         # do something with the exam
        # elif action == 'pre_clear':
        #     # handle the case where the m2m field is being cleared
        #     # do something before the m2m field is cleared
        # elif action == 'post_clear':



# Course Static Create Defualt values;
@receiver(post_save, sender=ExamProgram)
def calculate_attending(sender, instance, created, **kwargs):
    traker = ExamProgram.objects.get(date=instance.date,ec=instance.ec).tracker
    if traker:
        is_submited=True
    else: 
        is_submited =False
    ss = ExamProgram.objects.get(date=instance.date,ec=instance.ec)
    
    # if created:
    #      for i in ss.course.all():
    #         if not CourseStatistics.objects.filter(course=i, ec=instance.ec).exists():
    #             CourseStatistics.objects.create(course=i,ec=instance.ec,average_grade=0,max_grade=0,min_grade=0,grade_count=0,is_submited=is_submited)

    if not created:
     for i in ss.course.all():
        if CourseStatistics.objects.filter(course=i, ec=instance.ec).exists():
            CourseStatistics.objects.update_or_create(
                course=i, ec=instance.ec,
                defaults={'is_submited':is_submited }
        )

# static system
@receiver(post_delete,sender=studentCourse)
def calculate_statistics(sender, instance, created=True, **kwargs):
    gradesAggrigateCourse = studentCourse.objects.filter(courseId=instance.courseId,examCourse=instance.examCourse)
    GRAD_COURSE=studentCourse.objects.filter(courseId=instance.courseId)
    temp=[i.grad for i in GRAD_COURSE]
    temp.sort()
    occurrence = {item: temp.count(item) for item in temp}
    grade_count = gradesAggrigateCourse.count()

    if grade_count > 0:
        success_count = gradesAggrigateCourse.filter(grad__gte=60).count()
        success_rate = (success_count/grade_count)*100
        average_grade = gradesAggrigateCourse.aggregate(Avg('grad'))['grad__avg']
        max_grade = gradesAggrigateCourse.aggregate(Max('grad'))['grad__max']
        min_grade = gradesAggrigateCourse.aggregate(Min('grad'))['grad__min']
        grade_stddev = gradesAggrigateCourse.aggregate(StdDev('grad'))['grad__stddev']
        grade_variance = gradesAggrigateCourse.aggregate(Variance('grad'))['grad__variance']
        is_corrected = True
    else:
        success_rate=None
        average_grade = None
        max_grade = None
        min_grade = None
        grade_stddev = None
        grade_variance = None
        is_corrected = False
    if grade_count > 0:
        CourseStatistics.objects.update_or_create(
            course=instance.courseId, ec=instance.examCourse,
            defaults={'average_grade': average_grade, 'max_grade': max_grade, 'min_grade': min_grade, 'grade_count': grade_count  ,'grade_stddev':grade_stddev,
            'grade_variance':grade_variance,'is_corrected':is_corrected,'success_rate':success_rate}
        )
    else:
        CourseStatistics.objects.filter(course=instance.courseId,ec=instance.examCourse).delete()

@receiver(post_save, sender=studentCourse)
def calculate_statistics(sender, instance, created, **kwargs):
    gradesAggrigateCourse = studentCourse.objects.filter(courseId=instance.courseId,examCourse=instance.examCourse)
    GRAD_COURSE=studentCourse.objects.filter(courseId=instance.courseId)
    temp=[i.grad for i in GRAD_COURSE]
    temp.sort()
    occurrence = {item: temp.count(item) for item in temp}
    
    grade_count = gradesAggrigateCourse.count()
    success_count = gradesAggrigateCourse.filter(grad__gte=60).count()
    success_rate = (success_count/grade_count)*100
    if grade_count > 0:
        average_grade = gradesAggrigateCourse.aggregate(Avg('grad'))['grad__avg']
        max_grade = gradesAggrigateCourse.aggregate(Max('grad'))['grad__max']
        min_grade = gradesAggrigateCourse.aggregate(Min('grad'))['grad__min']
        grade_stddev = gradesAggrigateCourse.aggregate(StdDev('grad'))['grad__stddev']
        grade_variance = gradesAggrigateCourse.aggregate(Variance('grad'))['grad__variance']
        is_corrected = True
    else:
        average_grade = None
        max_grade = None
        min_grade = None
        grade_stddev = None
        grade_variance = None
        is_corrected = False
    CourseStatistics.objects.update_or_create(
        course=instance.courseId, ec=instance.examCourse,
        defaults={'average_grade': average_grade, 'max_grade': max_grade, 'min_grade': min_grade, 'grade_count': grade_count  ,'grade_stddev':grade_stddev,
        'grade_variance':grade_variance,'is_corrected':is_corrected,'success_rate':success_rate}
    )

# from django.conf import settings
# from django.core.mail import send_mail
# @receiver(post_save, sender=CourseStatistics)
# def calculate_statistics(sender, instance, created, **kwargs):
#     info = CourseStatistics.objects.get(course=instance.course,ec=instance.ec)
#     avg_g=info.average_grade
#     max_grade = info.max_grade
#     success_rate = info.success_rate
#     subject = f'Report aboute course : {info.course.name}'
#     message = f'''<div>
#                         <div style="background-color: #212529; color: green; text-align: center; font-size: xx-large;" >
#                             <a style="color: green;" href="http://127.0.0.1:8000/">AQAR</a>
#                         </div>
#                             <div style="display: flex;
#                                 justify-items: center; justify-content: center;
#                                 align-items: center;  background-color: #76b852;
#                                 height: 400px; margin-left: 10px; margin-right: 10px;
#                                 border-radius: 10px;">
#                                 <p>avg_g::{avg_g}</p>
#                                 <p>max_grade::{max_grade}</p>
#                                 <p>success_rate::{success_rate}</p>

#                             </div>
#                         <div style="background-color: #212529;">.</div>
#                     </div>'''
#     email_from =  settings.EMAIL_HOST_USER
#     recipient_list = ['hosenrast@gmail.com']
#     send_mail( subject, message, email_from, recipient_list ,html_message=message,fail_silently=False)
#     print(avg_g)

# @receiver(post_save, sender=studentCourse)
# def calculate_statistics(sender, instance, created, **kwargs):
#     studentCourses = studentCourse.objects.filter(studentId=instance.studentId,examCourse__year=instance.examCourse.year)
#     a=studentCourses.filter(examCourse__Semineter='1')
#     b=studentCourses.filter(examCourse__Semineter='2')
#     a1=a.filter(grad__lte=60)
#     as1=a.filter(grad__gte=60)
#     b1=b.filter(grad__lte=60)
#     bs2=b.filter(grad__gte=60)
#     is_suc_in_year= False
#     temp=0
    
#     for i in range(bs2.count()):
#         for j in range(a1.count()):
#             if a1[j].courseId == bs2[i].courseId:
#                 temp=temp+1

#         num_of_succ_course = as1.count()+bs2.count()
#         year = studentCourses[0].studentId.academic_year
#         to_year = int(studentCourses[0].studentId.academic_year)+1
#         if year ==1:
#             num_of_course_remain = 14-(as1.count()+bs2.count())
#             if 14-(as1.count()+bs2.count())<= 4:
#                 # to_year=year+1
#                 is_suc_in_year = True
#             else:
#                 is_suc_in_year = False
#         if year in [2,3,4]:
#             num_of_course_remain = 12-(as1.count()+bs2.count())
#             if 12-(as1.count()+bs2.count())<= 4:    
#                 is_suc_in_year = True
#             else:
#                 is_suc_in_year = False
#         if year == 5:
#             num_of_course_remain = 10-(as1.count()+bs2.count())
#             if 10-(as1.count()+bs2.count())<= 4:
#                 to_year=5
#                 is_suc_in_year = True
#             else:
#                 is_suc_in_year = False


#     Student_Course_Suc.objects.update_or_create(
#         stu=instance.studentId,
#         defaults={'is_suc_in_year': is_suc_in_year, 'num_of_course_remain': num_of_course_remain, 'num_of_succ_course': num_of_succ_course, 'year': year  ,'to_year':to_year,'year_exam':studentCourses[0].studentId.year_exam})



# level up sysytem
@receiver(post_save,sender=Student)
def calculate_statistics(sender, instance, created, **kwargs):
    stu = Student.objects.filter(id=instance.id)
    crs =Course.objects.filter(year=str(stu[0].academic_year))
    if created:
        for i in crs:
            CourseDemands.objects.update_or_create(
            stu=instance,
            courseId=i)
    if not created and stu[0].is_level_up:
        stu = Student.objects.filter(id=instance.id).update(is_level_up=False)
        for i in crs:
            CourseDemands.objects.update_or_create(
            stu=instance,
            courseId=i)



@receiver(post_save,sender=studentCourse)
def calculate_statistics(sender, instance, created, **kwargs):
    sc = studentCourse.objects.filter(courseId=instance.courseId,examCourse=instance.examCourse)
    for i in sc:
        if(i.IsSuccessed):
            CourseDemands.objects.filter(stu=i.studentId,courseId=i.courseId).delete()


# @receiver(post_save, sender=Student)
# def my_handler(sender, instance,created, **kwargs):
#     print('hi')
#     # if instance.pk and instance.academic_year!= Student.objects.get(pk=instance.pk).academic_year:
#     # if not created:
#         old_value = Student.objects.get(pk=instance.pk).academic_year
#         new_value = instance.academic_year
#         stu = Student.objects.filter(id=instance.id)
#         crs =Course.objects.filter(year=str(stu[0].academic_year))
#         print(old_value,new_value)
#         print(crs,stu)
#         # for i in crs:
#             # print(i.name)
#             # CourseDemands.objects.update_or_create(
#             # stu=instance,
#             # courseId=i)

@receiver(post_delete,sender=CourseDemands)
def calculate_statistics(sender, instance, created=False, **kwargs):
            cd = CourseDemands.objects.filter(stu=instance.stu)
            if cd.count() in [0,1,2,3]:
                pass
            elif cd.count()<=4 :
                if  instance.stu.Address is None:
                     instance.stu.Address=''
                if  instance.stu.email is None:
                     instance.stu.email=''
                if  instance.stu.phone is None:
                     instance.stu.phone=900000000
                stuUp= Student.objects.get(id=instance.stu.id).academic_year+1
                a = Student(id=instance.stu.id,
                firstName=instance.stu.firstName,
                lastName=instance.stu.lastName,
                academic_year=stuUp,
                is_level_up=True,
                Address=instance.stu.Address,
                email=instance.stu.email,
                phone=instance.stu.phone
                )
                a.save()
