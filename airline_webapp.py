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
    print "We have the correct route"
    try:
        # TODO: Insert some code that does something with airline
        airline = request.args['airline']
        answer = computeResultFromAirline(airline)
        print "airline=" + airline
        
        return render_template('airline_result.html',airline=airline,result=answer)
        # return "renderAirlineResult stub, result=" + result
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/airport_result')
def renderAirportResult():
   print "We are in the stub for render airport result"
   return "stub"

def computeResultFromAirline(airline):
    result = ""
    list_of_airline = airlines.get_reports()
    for a in list_of_airline:
        if a['carrier']['code']==airline:
            result += a['airport']['code']+" "
    return result

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)


    
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=54321)
