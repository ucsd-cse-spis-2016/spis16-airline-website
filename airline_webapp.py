import os
from flask import Flask, url_for, render_template, request

import airline_data_analysis

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('main_menu.html')

@app.route('/airport')
def renderAirport():
    return render_template('airport.html')

@app.route('/airline')
def renderAirline():
    return render_template('airline.html')

@app.route('/airline_result')
def renderAirlineResult():
    try:
        # TODO: Insert some code that does something with airline
        airline = request.args['airline']
        answer = computeResultFromAirline(airline)

        return render_template('airline_result.html',airline=airline,result=answer)
        # return "renderAirlineResult stub, result=" + result
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/airport_result')
def renderAirportResult():
    try:
        # TODO: Insert some code that does something with airline
        airport = request.args['airport']
        delayDictList = computeResultFromAirport(airport)
        
        return render_template('airport_result.html',airport=airport,answer=delayDictList)
        # return "renderAirlineResult stub, result=" + result
    except ValueError:
        return "Sorry: something went wrong."

def computeResultFromAirline(airline):
   return "stub"

def computeResultFromAirport(airport):
     data = airline_data_analysis.getData()
     print "we are in computeResultFromAirport"
     print "len(data)=", len(data)
     data_for_this_airport = airline_data_analysis.dataForAirport(data,airport)
     print "we are after data_for_this_airport"
     
     print "len(data_for_this_airport)",len(data_for_this_airport)
     delayDictList = map(airline_data_analysis.delayDict, data_for_this_airport)
     print "len(delayDictList)",len(delayDictList)
     return delayDictList
    
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=54321)
