from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE = (('W','여성'),('M','남성'))
# SLEEP_HABIT_CHOICE = (('A','이 갈이'),('B','코골이'))
# SLEEP_TIME_CHOICE = (('D','D'),('E','E'),('F','F'),)
# CLEAN_CHOICE = (('G','G'),('H','H'),('I','I'),)
# COOK_CHOICE = (('J','J'),('K','K'),('L','L'),)
# BUDGET_CHOICE = (('M','M'),('N','N'),('O','O'),)
SMOKER = (('N','비흡연자'),('Y','흡연자'))

class UserInfo(AbstractUser):
    profile_img = models.ImageField(upload_to ="common/", blank=True, null =True)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE,default='W')
    age = models.IntegerField(default=0)
    school = models.CharField(max_length=30)
    major = models.CharField(max_length=50)
    studentID =models.IntegerField(default=0)
    sleep_habit = models.CharField(max_length=50)
    sleep_time = models.TimeField(auto_now=False)
    cleanliness = models.CharField(max_length=50)
    cook = models.CharField(max_length=50)
    smoke =  models.CharField(max_length=10, choices=SMOKER, default='비흡연자')
    budget = models.CharField(max_length=50)
    hope_area = models.CharField(max_length=50)
    introduction = models.CharField(max_length=100)
    profile_active = models.BooleanField(default=True)
