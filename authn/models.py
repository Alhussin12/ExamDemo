from django.db import models
from django.contrib.auth.models import User
# Create your models here.
roles=(
    ('Deanship','Deanship'),
    ('ExamDepatment','ExamDepatment'),
    ('PresidencyUniversity','PresidencyUniversity')
)

class ExamUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(choices=roles,null=False)

    def __str__(self):
        return str(self.user.username) +' '+str(self.role)
