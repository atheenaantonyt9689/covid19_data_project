#from collections import Counter

    
from .models import CovidCases
from django.views import View
from django.shortcuts import render
class HomePageView(View):
    model=CovidCases
    def get(self,request,*args,**kwargs):      

        covid_dataset=CovidCases.objects.all()        
        counts=dict()
        
        for case in covid_dataset:  
                state_dict=counts.get(case.state) or dict(active=0,confirmed=0,deceased=0,recovered=0)
                exsisting_active_count=state_dict['active']  
                exsisting_confirmed_count=state_dict['confirmed'] 
                exsisting_deceased_count=state_dict['deceased']  
                exsisting_recovered_count=state_dict['recovered']      



                new_active_count=exsisting_active_count +int(case.active) 
                new_confirmed_count=exsisting_confirmed_count+int(case.confirmed)
                new_deceased_count=exsisting_deceased_count+int(case.deceased)
                new_recovered_count=exsisting_recovered_count+int(case.recovered)               

                counts.update({ case.state:dict(active=new_active_count,confirmed=new_confirmed_count,deceased=new_deceased_count,recovered=new_recovered_count)})   
                
        print(counts)  
        context={  
                
            "counts":counts,          
        }
        return render(request,"core_section/home.html",context)

            
        
        
    

