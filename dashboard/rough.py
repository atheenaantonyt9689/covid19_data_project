




































active_dictionary={'State Unassigned': {'active': 0}, 
'Andaman and Nicobar Islands': {'active': 224},
'Andhra Pradesh': {'active': 170588},
'Arunachal Pradesh': {'active': 1777}, 
'Assam': {'active': 29088}, 
'Bihar': {'active': 113479}, 'Chandigarh': {'active': 8363},
'Chhattisgarh': {'active': 129211},
'Delhi': {'active': 90629}, 
'Dadra and Nagar Haveli and Daman and Diu': {'active': 1708},
'Goa': {'active': 27964}
}
from collections import OrderedDict

ordered = OrderedDict(sorted(active_dictionary.items(), key=lambda i: i[1]['active'], reverse=True))
print(ordered)


#test_dict = {'Geeks' : 1, 'For':2,  'is' : 3, 'best' : 4, 'for' : 5, 'CS' : 6}
    
# printing original dictionary 
print("The original dictionary : " +  str(ordered)) 
    
# Initialize limit 
N = 3
    
# Using items() + list slicing 
# Get first K items in dictionary 
out = dict(list(ordered.items())[0: N]) 
        
# printing result  
print("Dictionary limited by K is : " + str(out)) 

