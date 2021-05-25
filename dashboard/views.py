#from django.views.generic.base import TemplateView
#from collections import OrderedDict
from django import views
from django.db.models import Sum
from django.db import models
from django.db.models.sql.query import RawQuery
#from django.http.response import HttpResponse
#from django.views.generic.base import TemplateView
from .models import CovidDistrict
from django.views import View
from django.shortcuts import render
class HomePageView(View):
    model=CovidDistrict
    template_name='core_section/home.html'
    def get(self,request,*args,**kwargs):         

        state_total_data=CovidDistrict.objects.values('state').annotate(Sum('active'),Sum('confirmed'),Sum('recovered'),Sum('deceased'))
        
        context={ 

                "state_total_data":state_total_data

        }           
        return render(request,"core_section/home.html",context)


class ActiveCasesViews(View):
    model=CovidDistrict
    Template_name="core_section/active_cases.html"

    def get(self,request,*args,**kwargs):    
        ordered_districts=CovidDistrict.objects.order_by('-active').values('state','district','active')[:10]
        #print(ordered_districts)            
        context={
            "ordered_districts":ordered_districts
                     

        }           
        return render(request,"core_section/active_cases.html",context)


class DistrictViews(View):    
    model=CovidDistrict
    Template_name="core_section/state_page.html"
    def get(self,request,*args,**kwargs):

        state_covid=request.GET.get("state")
        state_covid_data=CovidDistrict.objects.filter(state="state_covid").order_by('-active').values('state','district','active')[:5]
            
        
        #print(state_covid_data)
        
        context={
            "state_covid_data":state_covid_data
        
        }  
         
        return render(request,"core_section/state_page.html",context)



class SearchView(View):
    model=CovidDistrict
    template_name='core_section/search_page.html'
    def get(self,request,*args,**kwargs): 

        val = self.request.GET.get("district") 
       
        if val:
            queryset = CovidDistrict.objects.filter(district__iexact=val).values('state','district','active','confirmed','recovered','deceased')
            print("query set:",queryset)
        else:
            queryset = CovidDistrict.objects.none()
            #print("District not found")
        


        
        context={ 

                "queryset":queryset

        }           
        return render(request,"core_section/search_page.html",context)



        


            
        
        
    

