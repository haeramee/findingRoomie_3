from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from django.forms.widgets import RadioSelect
from .models import UserInfo 

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'password1','password2','nickname','gender','age','school','major',
        'studentID','sleep_habit','sleep_time','cleanliness',
        'cook','smoke','budget','hope_area','introduction',
        'profile_active','profile_img',
        ]
        widgets = {
            'introduction': forms.Textarea(attrs={'rows':'3', 'cols': '40', 'placeholder':' 한 줄 자기 소개'}),
            'gender':forms.Select(),
            'sleep_habit':forms.Select(),
            'sleep_time': forms.Select(),
            'cleanliness':forms.Select(),
            'cook':forms.Select(),
            # 'budget':forms.RadioSelect(),
        }

