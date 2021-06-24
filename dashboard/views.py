#from django.views.generic.base import TemplateView
#from collections import OrderedDict
#from dateutil import parser
from datetime import datetime
from django import views
from django.db.models import Sum
from django.db import models
from django.db.models.sql import query
from django.db.models.sql.query import RawQuery
from .models import CovidDistrict
from django.views import View
from django.shortcuts import render
def get_published_dates():
    all_dates=CovidDistrict.objects.order_by("published_date").values('published_date').distinct()
    return all_dates

def get_latest_date():
    latest_date=CovidDistrict.objects.order_by("-published_date").values('published_date')[:1]
    return latest_date[0]["published_date"]

def get_state_data(pub_date):
    state_total_data=CovidDistrict.objects.filter(published_date=pub_date).values('state').annotate(Sum('active'),Sum('confirmed'),Sum('recovered'),Sum('deceased'))
    return state_total_data
        


class DateFilterView(View):
    #model=CovidDistrict
    template_name='dashboard/home.html'
    def get(self,request,*args,**kwargs):        
      
        all_dates=get_published_dates()
        latest_date=get_latest_date()
        state_total_data=get_state_data(latest_date)

           
        context={ 
            "all_dates":all_dates,
            "latest_date":latest_date,
            "state_total_data":state_total_data

               
        }           
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):         
        published_date=request.POST.get('published_date')
           
        query_date = datetime.strptime(published_date, '%B %d, %Y')
        state_total_data=get_state_data(query_date)
        all_dates=get_published_dates()     
         
          
        context={ 
            
            "state_total_data":state_total_data,
            "all_dates":all_dates
               
        }           
        return render(request,self.template_name,context)

class ActiveCasesViews(View):
    model=CovidDistrict
    Template_name="dashboard/active_cases.html"

    def get(self,request,*args,**kwargs): 
        latest_date=get_latest_date()         
        ordered_districts=CovidDistrict.objects.filter(published_date=latest_date).order_by('-active').values('state','district','active')[:10]
        print(ordered_districts)            
        
        context={
            "ordered_districts":ordered_districts ,
             "latest_date":latest_date              

        }           
        return render(request,self.Template_name,context)


class DistrictViews(View):    
    model=CovidDistrict
    Template_name="dashboard/state_page.html"
    def get(self,request,*args,**kwargs):
        latest_date=get_latest_date()
        state_covid=request.GET.get("state")        
        
        state_covid_data=CovidDistrict.objects.filter(state=state_covid,published_date=latest_date).order_by('-active').values('state','district','active')[:5]
         
        
        #print(state_covid_data)
        
        context={
            "state_covid_data":state_covid_data,
            "latest_date":latest_date
        
        }  
         
        return render(request,self.Template_name,context)



class SearchView(View):
    model=CovidDistrict
    template_name='dashboard/search.html'
    def get(self,request,*args,**kwargs):
        latest_date=get_latest_date() 
        
        val = self.request.GET.get("district") 
       
        if val:
            queryset = CovidDistrict.objects.filter(district__iexact=val,published_date=latest_date).values('state','district','active','confirmed','recovered','deceased','published_date').order_by('-published_date') 
            print("query set:",queryset)
        else:
            queryset=None
            


        
        context={ 
                "queryset":queryset,
               "val":val

        }           
        return render(request,self.template_name,context)



        


            
        
        
    

