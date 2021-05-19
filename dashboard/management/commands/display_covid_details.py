
from django.core.management.base import BaseCommand
from django.db.models.fields import DateField
from dashboard.models import CovidDistrict
import requests
import json


class Command(BaseCommand):
    help = 'display_covid_details'

    def handle(self, *args, **kwargs):
        
        url="https://api.covid19india.org/state_district_wise.json"
        response=requests.get(url).text
        response_info=json.loads(response)
        #res=dict()
        for state, state_data in response_info.items():
            district_info =state_data['districtData']
            ditricts=district_info.keys()
            length=len(ditricts)
            
            for district_name,district_values in district_info.items(): 
                #print(district_name)


                obj1=CovidDistrict.objects.create(state=state,district=district_name,active=district_values['active'],confirmed=district_values['confirmed'],deceased=district_values['deceased'],recovered=district_values['recovered'])
                obj1.save()



                #print(state,district_name,district_values['active'],district_values['confirmed'],district_values['deceased'],district_values['recovered'])
        

        