from __future__ import print_function

# import airline data from https://think.cs.vt.edu/corgis/
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

def airline_dict(data):
    result = {}
    for a in data:
        airline_code = a['carrier']['code']
        result[airline_code] = a['carrier']['name']
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

def percentDelayed(oneReport):
    ''' given one report from data, compute % of flights delayed '''
    return 100.0 * float(oneReport['statistics']['flights']['delayed'])/float(oneReport['statistics']['flights']['total'])

def getData():
    return airlines.get_reports(test=False) # big data

def dataForAirport(data,airport):
    result = []
    for d in data:
      if d['airport']['code']==airport:
        result.append(d)
    return result

def delayDict(oneReport):
    return { 'airport_code' : oneReport['airport']['code'],
             'airline_code' : oneReport['carrier']['code'],
             'percentDelayed' : percentDelayed(oneReport),
             'delayed' : oneReport['statistics']['flights']['delayed'],
             'total' : oneReport['statistics']['flights']['total'],
             'yyyy_m' : oneReport['time']['label']}

if __name__=="__main__":
    # data = airlines.get_reports(test=False) # big data
    sdata = airlines.get_reports(test=True) # small data 
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
   airline_dict(data)
   iterate_airports(airport_dict(data),printAirport)
   iterate_airports(airport_dict(data),printAirportNicely)
   """)


