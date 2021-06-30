from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['nickname','username','profile_img','gender',
        'age','school','major','studentID','sleep_habit','sleep_time',
        'cleanliness','cook','smoke','budget','hope_area',
        'introduction','profile_active',
        ]
