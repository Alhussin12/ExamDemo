from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils import timezone
from datetime import datetime

# Create your models here.
SEMINETER_CHOICES = (
    ("1", "First"),
    ("2", "Second"),
    ("3", "Thered"),
)
DEPARTMENT_CHOICES = (
    ("NetWork", "network"),
    ("Software", "software"),
)
TYPE_COURSE_CHOICES = (
    ("Automated", "automated"),
    ("Written ", "written "),
)
YEAR_COURSE_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4",'4'),
    ('5','5')
)
class Instractor(models.Model):
    firstName = models.CharField(max_length=50,null=False)
    lastName = models.CharField(max_length=50,null=False)
    mobile = models.IntegerField(validators=[MinValueValidator(900000000),MaxValueValidator(958604093)],null=True,blank=True)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return self.firstName + " " +self.lastName
    class Meta:
        ordering = ["firstName","lastName"]



class ExamCourse(models.Model):
  
    Semineter =models.CharField(choices=SEMINETER_CHOICES,null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateTimeField(null=False)
    year= models.IntegerField(default=0,editable=True)
    inProgress =models.BooleanField(default=True) 

    def save(self, *args, **kwargs):
        if self.end_date.date()<= timezone.now().date():
            self.inProgress = False
        else:
            self.inProgress=True

        super(ExamCourse, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.start_date.year)+"/"+ str(self.start_date.month)+'/'+ str(self.start_date.day)+ " Semineter(" + str(self.Semineter)+')'
    class Meta:
        ordering = ['-start_date']
        # unique_together = [['start_date', 'Semineter']]
        


class Course(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(choices=YEAR_COURSE_CHOICES,null=False)
    dept = models.CharField(choices=DEPARTMENT_CHOICES,null=True,blank=True)
    type = models.CharField(choices=TYPE_COURSE_CHOICES,null=False)
    instractor = models.ManyToManyField(Instractor)

    def __str__(self):
        return self.name
    def exams_set(self):
        return ExamCourse.objects.filter(course=self)

class Student(models.Model):
    # year_exam = models.ForeignKey(Year_Exam,on_delete=models.CASCADE,null=True)
    firstName = models.CharField(max_length=50,null=False)
    lastName = models.CharField(max_length=50,null=False)
    Address = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.IntegerField(validators=[MinValueValidator(900000000),MaxValueValidator(958604093)],null=True,blank=True)
    academic_year = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)],null=True)
    is_level_up=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName + " " + str(self.id)
    class Meta:
        ordering=['academic_year','firstName']

class studentCourse(models.Model):
    studentId = models.ForeignKey(Student, related_name='courses',on_delete=models.CASCADE)
    courseId = models.ForeignKey(Course,related_name='students',on_delete=models.CASCADE)
    examCourse = models.ForeignKey(ExamCourse,on_delete=models.CASCADE)
    grad = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)] ,null=True,blank=True)
    IsSuccessed = models.BooleanField(default=False,editable=True)
    isAttended = models.BooleanField(default=None,editable=True)
    corrected_date = models.DateField(blank=True,null=True)

    def save(self, *args, **kwargs):

        if self.grad == None:
            self.isAttended=False
            self.IsSuccessed=False
        else:
            self.corrected_date = datetime.now().date()
            self.isAttended=True
            if self.grad >= 60:
                self.IsSuccessed=True
            else:
                self.IsSuccessed=False
        super(studentCourse, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.courseId.name + ' '+ self.studentId.firstName + ' ' + self.studentId.lastName +' '+ str(self.studentId.id) + ' ' +str(self.grad)
    class Meta:
        unique_together = [['courseId', 'studentId','examCourse']]
        ordering = ['courseId']


class courseStatus(models.Model):
    isCorrected = models.BooleanField(default=False)
    correctionScale = models.BooleanField(default=False)
    IsQuestionSubmited = models.BooleanField(default=False)
    course = models.ForeignKey(studentCourse,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.course.name

class InstCourse(models.Model):
    instId = models.ForeignKey(Instractor,on_delete=models.CASCADE)
    CourseId = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.instId.firstName + ' ' + self.instId.lastName + ' ' + self.CourseId.name
    class Meta:
        unique_together = [['instId', 'CourseId']]

class ExamProgram(models.Model):
    ec=models.ForeignKey(ExamCourse,on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    date=models.DateField()
    time=models.TimeField()
    tracker = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if timezone.now().date() >= self.date:
            self.tracker=True
        else:
            self.tracker=False
        super(ExamProgram, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return str(self.ec.start_date.year) + '    ' + str(self.date)
    class Meta:
        unique_together = ['ec','date']

class StudentsStatistics(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)
    ec = models.ForeignKey(ExamCourse, on_delete=models.CASCADE)
    average_grade = models.FloatField()
    max_grade = models.FloatField()
    min_grade = models.FloatField()
    grade_count = models.IntegerField()
    success_grades_count = models.IntegerField(default=0)
    grade_stddev = models.FloatField(default=0)
    grade_variance = models.FloatField(default=0)
    def __str__(self):
        return "SeraialNumber: ("+str(self.stu.id) + ")__Name: " + str(self.stu.firstName) +' '+ str(self.stu.lastName) + " __ExameCourse: " + str(self.ec.start_date.year) +' ('+str(self.ec.Semineter)+')'
    class Meta :
        unique_together=['stu','ec']
        ordering = ['stu']

class CourseStatistics(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ec = models.ForeignKey(ExamCourse, on_delete=models.CASCADE)
    average_grade = models.FloatField()
    max_grade = models.FloatField()
    min_grade = models.FloatField()
    grade_count = models.IntegerField()
    grade_stddev = models.FloatField(default=0)
    grade_variance = models.FloatField(default=0)
    success_rate=models.FloatField(default=0)
    is_submited = models.BooleanField(default=False)
    is_corrected = models.BooleanField(default=False)
    is_Correcten_Scale_submited = models.BooleanField(default=False)
    is_Question_submited =models.BooleanField(default=False)
    corrected_date = models.DateField(blank=True,null=True)
    submited_date = models.DateField(blank=True,null=True)

    def save(self, *args, **kwargs):

        if self.is_corrected:
            self.corrected_date = datetime.now().date()
        if self.is_submited:
            self.is_Question_submited =True
            self.submited_date = datetime.now().date()

        super(CourseStatistics, self).save(*args, **kwargs)


    def __str__(self):
        return "SeraialNumber: ("+str(self.course.id) + ")__Name: " + str(self.course.name) +' '+ " __ExameCourse: " + str(self.ec.start_date.year) +' ('+str(self.ec.Semineter)+')'
    class Meta :
        unique_together=['course','ec']
        ordering = ['-course']

class CourseDemands(models.Model):
    stu=models.ForeignKey(Student,on_delete=models.CASCADE)
    courseId= models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  str(self.stu.firstName) + ' ' + str(self.courseId.name)

class StudentFullReport(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='pdf/')