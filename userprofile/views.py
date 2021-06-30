# from typing_extensions import Required
from django.shortcuts import redirect, render,get_object_or_404
from common.models import *
from .forms import *

def home(request):
    users = UserInfo.objects.all()
    return render(request,'home.html',{'users':users})

def MyProfile(request):
    profile = UserInfo.objects.get(pk=request.user.pk)

    if not profile.profile_img:
        img_url = ""
    else:
        img_url = profile.profile_img.url
    
    context={
        'username' : profile.username,
        'nickname':profile.nickname,
        'gender':profile.gender,
        'age':profile.age,
        'major':profile.major,
        'studentID':profile.studentID,
        'introduction':profile.introduction,
        'profile_img' :img_url,
        'sleep_time':profile.sleep_time,
        'cleanliness':profile.cleanliness,
        'cook':profile.cook,
        'smoke':profile.smoke,
        'budget':profile.budget,
        'hope_area':profile.hope_area,
        'profile_active':profile.profile_active,
    }
    return render(request,'MyPage.html',{'context':context})
    
def edit(request,pk):
    if request.method == 'POST':
        # 이미지 파일 수정 안되는거 오류 해결 필요
        form=CustomUserChangeForm(request.POST,instance=request.user,)
        if form.is_valid():
            form.save()
        return redirect("MyPage")
    else:
        form = CustomUserChangeForm(instance = request.user)
        return render(request,'edit.html',{'form':form})



def search(request):
    users = UserInfo.objects.all().order_by('username')

    q = request.POST.get('q', "") 

    if q:
        variable_column = request.POST.get('fd_name')
        if variable_column=="major":
            users = users.filter(major__icontains=q)
        else :
            users = users.filter(hope_area__icontains=q)

        return render(request, 'search.html', {'users' : users, 'q' : q})
    
    else:
        return redirect(request, home)


def detail(request,id):
    users = get_object_or_404(UserInfo,pk=id)
    return render(request,'detail.html',{'users':users})
