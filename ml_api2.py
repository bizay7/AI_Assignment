# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:49:19 2022

@author: BijayaP
"""

from fastapi import FastAPI
import joblib
import numpy as np


app = FastAPI()

@app.get("/greet")
def greet():
    print("Get Method being called")
    return {'hello': 'world'}

@app.post("/satisfaction_prediction1")
def satisfaction_predd(Age : int, Flight_Distance : int,
Inflight_wifi_service : int, Departure_Arrival_time_convenient : int,
Ease_of_Online_booking : int, Gate_location : int, Food_and_drink : int,
Online_boarding : int, Seat_comfort : int, Inflight_entertainment : int,
On_board_service : int, Leg_room_service : int, Baggage_handling : int,
Checkin_service : int, Inflight_service : int, Cleanliness : int,
Departure_Delay_in_Minutes : int, Arrival_Delay_in_Minutes : float):
    
    satisfaction_model = joblib.load('satisfaction_model')
    input_data_array = np.asarray([Age, Flight_Distance, Inflight_wifi_service, Departure_Arrival_time_convenient,
Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding, Seat_comfort,
Inflight_entertainment, On_board_service, Leg_room_service, Baggage_handling, Checkin_service,
Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes])
    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = satisfaction_model.predict(input_data_reshaped)
    
    if (prediction[0] == 0):
        return 'The person is not satisfied'
    else:
        return 'The person is satisfied'