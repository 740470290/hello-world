from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
user_list=[]
def index(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        sex=request.POST.get("sex",None)
        feature1=request.POST.get("feature1",None)
        feature2=request.POST.get("feature2",None)
        feature3=request.POST.get("feature3",None)
        feature4=request.POST.get("feature4",None)
        models.UserInfo.objects.create(user=username,pwd=password,sex=sex,feature=feature1+str(feature2)+str(feature3)+str(feature4))
    user_list=models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})