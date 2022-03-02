# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:18:03 2021

@author: horowitz-b
"""

import requests
import json

# enter your api key here 
api_key ='AIzaSyBcKOgGNfC5qiSMKeC7M2JzMvmrX2gXb5s'

# Take source as input 
#source = input() 
source = '1200 travis'  
# Take destination as input 
#dest = input() 
dest = '26630 green heron dr'  
# url variable store url  
#url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?&origins=source&destinations=dest&key=api_key'
  
# Get method of requests module 
# return response object 
r = requests.get(url + 'origins = ' + source +
                   '&destinations = ' + dest +
                   '&key = ' + api_key) 
                     
# json method of response object 
# return json format result 
x = r.json() 
  
# by default driving mode considered 
  
# print the value of x 
print(x) 