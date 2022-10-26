from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from classroomapp.models import Login, courseadd, teacherlogin, studentadd, notificationadd, stdleaveshedule, \
    tchrleaveshedule, Complaint, addnotes, taddAsgnmnttopic, SaddAssignments


class DateInput(forms.DateInput):
    input_type="date"

class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2= forms.CharField(widget=forms.PasswordInput, label='confirm password')
    class Meta:
        model=Login
        fields=('username','password1','password2',)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class userloginform(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model=teacherlogin
        fields=('name','age','address','subject','phone','tid','gender','image')

class courseddform(forms.ModelForm):
   # date=forms.DateField(widget=DateInput)
    class Meta:
        model=courseadd
        fields=('dept','subject','teacher','description')

class studentloginform(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model=studentadd
        fields=('name','dob','age','address','semester','dept','phone','sid','gender','photo')

class notificationform(forms.ModelForm):

    class Meta:
        model=notificationadd
        fields=('name','description')

class stdleavesheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:

        model=stdleaveshedule
        fields=('title','date','content')

class tchrleavesheduleform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:

        model=tchrleaveshedule
        fields=('title','date','content')


class ComplaintForm(forms.ModelForm):
    # date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('subject', 'complaint')


class notesddform(forms.ModelForm):
    class Meta:
        model=addnotes
        fields=('subject','title','description','file')


class taddAsgnmnttopicform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=taddAsgnmnttopic
        fields=('subject','title','date')


class sAssignmentddform(forms.ModelForm):

    class Meta:
        model=SaddAssignments
        fields=('subject','title','file')






