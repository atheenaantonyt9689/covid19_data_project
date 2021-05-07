from .models import CovidCases
from django.views import View
from django.shortcuts import render
class HomePageView(View):
    model=CovidCases
    def get(self,request,*args,**kwargs):       
        context={}        

        context["covid_dataset"]=CovidCases.objects.all()
        

        return render(request,"core_section/home.html",context)

    def post(self,request,*args,**kwargs):

        return render(request,"core_section/home.html",)




