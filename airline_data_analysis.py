from __future__ import print_function

import airlines

def airline_to_airports(data,airline):
    result = set()
    for a in data:
        if a['carrier']['code']==airline:
            result.add(a['airport']['code'])
    return list(result)

def airport_to_airlines(data,airport):
    result = set()
    for a in data:
        if a['airport']['code']==airport:
            result.add(a['carrier']['code'])
    return list(result)

def airport_dict(data):
    result = {}
    for a in data:
        airport_code = a['airport']['code']
        result[airport_code] = a['airport']['name']
    return result

def iterate_airports(airport_dict,fn):
    ''' fn is a function of the form fn(code,name)'''
    for code in airport_dict.keys():
        fn(code,airport_dict[code])

def printAirport(code,name):
    print (code,name)

def printAirportNicely(code,name):
    splitName = name.split(':')
    print (code.ljust(5),splitName[0].ljust(20),splitName[1])


if __name__=="__main__":
    data = airlines.get_reports(test=False)
    print ("""
Try:
   sdata = airlines.get_reports(test=True) # small data 
   data = airlines.get_reports(test=False) # big data
   airport_to_airlines(sdata,'SFO')
   airline_to_airports(sdata,'DL')
   airport_to_airlines(data,'SFO')
   airline_to_airports(data,'DL')
   len(data)
   data[0].keys()
   data[0]['some_key']
   airport_dict(data)
   iterate_airports(airport_dict(data),printAirport)
   iterate_airports(airport_dict(data),printAirportNicely)
   """)


