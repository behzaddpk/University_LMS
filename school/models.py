from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('Choose One', 'Choose One'),
        ('Computer Science','Computer Science'), 
        ('Electrical Engineering','Electrical Engineering'), 
        ('Mechanical Engineering','Mechanical Engineering'), 
        ('Information Technology','Information Technology'),]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=100, choices=classes,default='Choose One')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name




class Lecture(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=100, choices=classes, default='Choose One')
    video_file = models.FileField(upload_to='lecture_videos/')
    date_uploaded = models.DateField(auto_now_add=True)
    uploaded_by = models.ForeignKey(TeacherExtra, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=100)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)


