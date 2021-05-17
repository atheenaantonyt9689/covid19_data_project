"""var = a = { 
  'Black': { 'grams': 1906, 'price': 2.05},
  'Blue': { 'grams': 9526, 'price': 22.88},
  'Gold': { 'grams': 194, 'price': 8.24},
  'Magenta': { 'grams': 6035, 'price': 56.69},
  'Maroon': { 'grams': 922, 'price': 18.76},
  'Mint green': { 'grams': 9961, 'price': 63.89},
  'Orchid': { 'grams': 4970, 'price': 10.78},
  'Tan': { 'grams': 6738, 'price': 50.54},
  'Yellow': { 'grams': 6045, 'price': 54.19}
}

from collections import OrderedDict

ordered = OrderedDict(sorted(a.items(), key=lambda i: i[1]['price']))
print(ordered)"""





































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


