#from django.views.generic.base import TemplateView
#from collections import OrderedDict
from django.db.models import Sum
from django.db import models
from .models import CovidDistrict
from django.views import View
from django.shortcuts import render
class HomePageView(View):
    model=CovidDistrict
    def get(self,request,*args,**kwargs):      

        #covid_dataset=CovidDistrict.objects.all()
        
        state_total_data=CovidDistrict.objects.values('state').annotate(Sum('active'),Sum('confirmed'),Sum('recovered'),Sum('deceased'))
        #for i in state_total_data:
            #print(i)
        

       #
                  
        context={  
                "state_total_data":state_total_data

        }           
        return render(request,"core_section/home.html",context)


class ActiveCasesViews(View):
    model=CovidDistrict
    Template_name="core_section/active_cases.html"

    def get(self,request,*args,**kwargs):
        covid_data=CovidDistrict.objects.all()
        #sorted_list=sorted(covid_data,key=lambda k: int(k.active),reverse=True)


        ordered_districts=CovidDistrict.objects.order_by('-active').values('state','district','active')[:10]
        for i in ordered_districts:
            print(i)
        
        #ordered_districts_list=ordered_districts[0:9]  
        
            
        

        
        context={
            
            "ordered_districts":ordered_districts,
            #"ordered_districts_list":ordered_districts_list

        }           
        return render(request,"core_section/active_cases.html",context)





    


    




            
        
        
    

