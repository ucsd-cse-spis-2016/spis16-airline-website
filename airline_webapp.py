import os
from flask import Flask, url_for, render_template, request

import airlines


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
        answer = computeResultFromAirport(airport)
        
        return render_template('airport_result.html',airport=airport,answer=answer)
        # return "renderAirlineResult stub, result=" + result
    except ValueError:
        return "Sorry: something went wrong."

def computeResultFromAirline(airline):
    result = ""
    list_of_airline = airlines.get_reports(test=False)
    for a in list_of_airline:
        if a['carrier']['code']==airline:
            result += a['airport']['code']+" "
    return result

def computeResultFromAirport(airport):
    result = []
    list_of_airline = airlines.get_reports(test=False)
    for a in list_of_airline:
        if a['airport']['code']==airport:
            result.append(a)
    print a
    return result

    
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=54321)
