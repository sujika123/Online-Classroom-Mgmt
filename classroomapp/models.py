from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)


SUBJECT_CHOICES={
    ('MATHS','MATHS'),
    ('ENGLISH','ENGLISH'),
    ('DBMS','DBMS'),
    ('DCS','DCS'),
    ('MBD','MBD'),
    ('SP','SP'),
}


class teacherlogin(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name='teacher')
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(max_length=200)
    subject=models.CharField(max_length=30,choices=SUBJECT_CHOICES)
    phone=models.IntegerField(null=True,blank=True)
    tid=models.CharField(max_length=30)
    gender=models.CharField(max_length=100)
    image=models.ImageField()
    status=models.IntegerField(default=0)

class courseadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    dept = models.CharField(max_length=30)
    subject = models.CharField(max_length=40)
    teacher = models.CharField(max_length=50)
   # date = models.DateField()
    description = models.TextField(max_length=200, null=True, blank=True)
     #   image = models.ImageField()

class studentadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=200)
    semester = models.CharField(max_length=30)
    dept = models.CharField(max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    sid = models.CharField(max_length=30)
    gender = models.CharField(max_length=100)
    photo = models.ImageField()

class notificationadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
         return self.name


class stdleaveshedule(models.Model):
    name=models.CharField(max_length=100)
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    # status = models.BooleanField(default=False)
    status = models.IntegerField(default=0)


    def __str__(self):
         return self.name


class tchrleaveshedule(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Login,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    # status = models.BooleanField(default=False)
    status = models.IntegerField(default=0)

    def __str__(self):
         return self.name


class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    complaint = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)

    def __str__(self):
      return self.user

class addnotes(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to=None, max_length=254)


    # def __str__(self):
    #      return self.user


class taddAsgnmnttopic(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.DateField()

class SaddAssignments(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    file = models.FileField()
    date = models.DateField(auto_now=True)

    def __str__(self):
         return self.user
