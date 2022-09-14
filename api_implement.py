# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:54:07 2022

@author: BijayaP
"""

import json
import requests

#for testing
url = 'http://127.0.0.1:8000/satisfaction_prediction'

input_data_for_model = {
    'Age' : 52,
    'Flight_Distance' : 160,
    'Inflight_wifi_service' : 5,
    'Departure_Arrival_time_convenient' : 5,
    'Ease_of_Online_booking' : 5,
    'Gate_location' : 5,
    'Food_and_drink' : 5,
    'Online_boarding' : 5,
    'Seat_comfort' : 5,
    'Inflight_entertainment' : 5,
    'On_board_service' : 5,
    'Leg_room_service' : 5,
    'Baggage_handling' : 5,
    'Checkin_service' : 5,
    'Inflight_service' : 5,
    'Cleanliness' : 5,
    'Departure_Delay_in_Minutes' : 50,
    'Arrival_Delay_in_Minutes' : 44.0    
    
    }
input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.json())