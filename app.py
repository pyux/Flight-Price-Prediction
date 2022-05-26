from datetime import date
from sqlite3 import Date
from fastapi import FastAPI, Request, Query
import datetime
import uvicorn
import pickle

app = FastAPI()
 
@app.get('/')
def home():
    return {"Flight Prediction" : 'Price'}
   
@app.get('/predict')
def flight(duration : int,
    stop : int,
    date_of_journey : str = Query(None, description= "Enter your date of journey (DD/MM/YYYY)"),
    airline : str = Query('Air India',enum = ['Air India', 'Vistara','StarAir','Trujet','Indigo','GO FIRST','AirAsia','SpiceJet']),
    classs : str = Query('Class', enum = ['Business','Economy']),
    departure_time : str = Query('Departure', enum =['Early Morning','Morning','Afternoon','Evening','Night','Late Night']),
    arrival_time : str = Query('Arrival', enum = ['Early Morning','Morning','Afternoon','Evening','Night','Late Night'] ),
    Travelling_Cities : str = Query('Cities', enum = ['Bangalore-Chennai','Bangalore-Delhi','Bangalore-Hyderabad','Bangalore-Kolkata',
            'Bangalore-Mumbai','Chennai-Bangalore','Chennai-Delhi','Chennai-Hyderabad','Chennai-Kolkata',
            'Chennai-Mumbai','Delhi-Bangalore','Delhi-Chennai','Delhi-Hyderabad','Delhi-Kolkata',
            'Delhi-Mumbai','Hyderabad-Bangalore','Hyderabad-Chennai','Hyderabad-Delhi','Hyderabad-Kolkata',
            'Hyderabad-Mumbai','Kolkata-Bangalore','Kolkata-Chennai','Kolkata-Delhi','Kolkata-Hyderabad',
            'Kolkata-Mumbai','Mumbai-Bangalore','Mumbai-Chennai','Mumbai-Delhi','Mumbai-Hyderabad',
            'Mumbai-Kolkata'])):

    today = datetime.date.today()
    date_of_journey = datetime.datetime.strptime(date_of_journey,"%d/%m/%Y").date()
    days_1 = date_of_journey - today
    days_left = (days_1.days)

    a = 0
    if (airline == 'Air India'):
        a = 0

    elif (airline =='Vistara'):
        a = 1

    elif (airline == 'SpiceJet'):
        a = 2

    elif (airline == 'AirAsia'):
        a = 3
    
    elif (airline == 'GO FIRST'):
        a = 4

    elif (airline =='Indigo'):
        a = 5

    elif (airline == 'TruJet'):
        a = 6
    
    elif (airline == 'StarAir'):
        a = 7

    else :
        {"Error":"No Airline"}

    b = 0
    if (classs == 'Business'):
        b = 0

    elif (classs == 'Economy'):
        b = 1

    else:
        {"Error": "No Class Input"}


    c = 0 
    if (departure_time == 'Early_Morning'):
        c = 0

    elif (departure_time == 'Morning'):
        c = 1
    
    elif(departure_time == 'Afternoon'):
        c = 2

    elif(departure_time == 'Evening'):
        c = 3

    elif(departure_time == 'Night'):
        c = 4

    elif (departure_time == 'Late Night'):
        c=5

    else:
        {'Error': 'No Input'}


    d = 0 
    if (arrival_time == 'Early_Morning'):
        d = 0

    elif (arrival_time == 'Morning'):
        d = 1
    
    elif(arrival_time == 'Afternoon'):
        d = 2

    elif(arrival_time == 'Evening'):
        d = 3

    elif(arrival_time == 'Night'):
        d = 4

    elif (arrival_time == 'Late Night'):
        d = 5

    else:
        {'Error': 'No Input'}


    e = 0
    if(Travelling_Cities == 'Bangalore-Chennai'):
        e = 0

    elif(Travelling_Cities == 'Bangalore-Delhi'):
        e = 1
    
    elif(Travelling_Cities == 'Bangalore-Hyderabad'):
        e = 2

    elif(Travelling_Cities == 'Bangalore-Kolkata'):
        e = 3

    elif(Travelling_Cities == 'Bangalore-Mumbai'):
        e = 4

    elif(Travelling_Cities == 'Chennai-Bangalore'):
        e = 5
    
    elif(Travelling_Cities == 'Chennai-Delhi'):
        e = 6

    elif(Travelling_Cities == 'Chennai-Hyderabad'):
        e = 7

    elif(Travelling_Cities == 'Chennai-Kolkata'):
        e = 8

    elif(Travelling_Cities == 'Chennai-Mumbai'):
        e = 9

    elif(Travelling_Cities == 'Delhi-Bangalore'):
        e = 10

    elif(Travelling_Cities == 'Delhi-Chennai'):
        e = 11

    elif(Travelling_Cities == 'Delhi-Hyderabad'):
        e = 12

    elif(Travelling_Cities == 'Delhi-Kolkata'):
        e = 13

    elif(Travelling_Cities == 'Delhi-Mumbai'):
        e = 14

    elif(Travelling_Cities == 'Hyderabad-Bangalore'):
        e = 15

    elif(Travelling_Cities == 'Hyderabad-Chennai'):
        e = 16

    elif(Travelling_Cities == 'Hyderabad-Delhi'):
        e = 17

    elif(Travelling_Cities == 'Hyderabad-Kolkata'):
        e = 18

    elif(Travelling_Cities == 'Hyderabad-Mumbai'):
        e = 19

    elif(Travelling_Cities == 'Kolkata-Bangalore'):
        e = 20

    elif(Travelling_Cities == 'Kolkata-Chennai'):
        e = 21

    elif(Travelling_Cities == 'Kolkata-Delhi'):
        e = 22

    elif(Travelling_Cities == 'Kolkata-Hyderabad'):
        e = 23

    elif(Travelling_Cities == 'Kolkata-Mumbai'):
        e = 24

    elif(Travelling_Cities == 'Mumbai-Bangalore'):
        e = 25

    elif(Travelling_Cities == 'Mumbai-Chennai'):
        e = 26

    elif(Travelling_Cities == 'Mumbai-Delhi'):
        e = 27

    elif(Travelling_Cities == 'Mumbai-Hyderabad'):
        e = 28

    elif(Travelling_Cities == 'Mumbai-Kolkata'):
        e = 29


    model = pickle.load(open("model_pkl", "rb"))

    make_pred = model.predict([[a,stop,b,c,d,days_left,duration,e]])

    output = round(make_pred[0],2)

    return{'Your Flight Price is {}'.format((int(output +(output*15/100))))}

    
if __name__ == '__main__':
    uvicorn.run(app)