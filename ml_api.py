# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:49:19 2022

@author: BijayaP
"""

from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import json

app = FastAPI()

class model_input(BaseModel):     
    Age : int
    Flight_Distance : int
    Inflight_wifi_service : int
    Departure_Arrival_time_convenient : int
    Ease_of_Online_booking : int
    Gate_location : int
    Food_and_drink : int
    Online_boarding : int
    Seat_comfort : int
    Inflight_entertainment : int
    On_board_service : int
    Leg_room_service : int
    Baggage_handling : int
    Checkin_service : int
    Inflight_service : int
    Cleanliness : int
    Departure_Delay_in_Minutes : int
    Arrival_Delay_in_Minutes : float
    
        
# loading the saved model


@app.get("/")
def greet():
    print("Get Method being called")
    return {'Hello orld'}

@app.post("/satisfaction_prediction")
def satisfaction_predd(data : model_input):
    print("HI")
    input_data = data.json()
    input_dictionary = json.loads(input_data)
    input_dictionary = data.dict()
    
    
    x3 = input_dictionary['Age']
    x6 = input_dictionary['Flight_Distance']
    x7 = input_dictionary['Inflight_wifi_service']
    x8 = input_dictionary['Departure_Arrival_time_convenient']
    x9 = input_dictionary['Ease_of_Online_booking']
    x10 = input_dictionary['Gate_location']
    x11= input_dictionary['Food_and_drink']
    x12 = input_dictionary['Online_boarding']
    x13 = input_dictionary['Seat_comfort']
    x14 = input_dictionary['Inflight_entertainment']
    x15 = input_dictionary['On_board_service']
    x16 = input_dictionary['Leg_room_service']
    x17 = input_dictionary['Baggage_handling']
    x18 = input_dictionary['Checkin_service']
    x19 = input_dictionary['Inflight_service']
    x20 = input_dictionary['Cleanliness']
    x21 = input_dictionary['Departure_Delay_in_Minutes']
    x22 = input_dictionary['Arrival_Delay_in_Minutes']
    

    satisfaction_model = joblib.load('satisfaction_model')

    
    input_list = [x3,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22]
    
    prediction = satisfaction_model.predict([input_list])
    
    if (round(prediction[0]) == 0):
        return 'The person is not satisfied',round(prediction[0])
    else:
        return 'The person is satisfied',round(prediction[0])