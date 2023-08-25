#modules:
import win32com.client as wincom                                  # For getting speech (voice) from the text #(pip install Pywin 32)
import requests                                                   # Get the network link activated for downloading data
import json                                                       # To read the data in a dictionary format

#action:

speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter the city for live Weather reports: ")         # Input from the user to collect data live from site
                                                                  # Setting the url to a variable for accessing
my_url = f"http://api.weatherapi.com/v1/current.json?key=2c67a0783cfa48b9b4b100126232008&q={city}"
                                                                  
data = requests.get(my_url)                                       # Using module to get data using API

# print(data.text)

wdic= json.loads(data.text)                                       # Converting string to json (Dictionary type data) (machine readable)

                                                                  # Parameters required
state = wdic["location"]["region"]
country = wdic["location"]["country"]
time= wdic["current"]["last_updated"]
atm = wdic["current"]["condition"]["text"]
wind = wdic["current"]["wind_kph"]
temp = wdic["current"]["temp_c"]

data_say= (f" The State of your {city} is : {state} and Country is  {country}." \
           f"\n The temperature is {temp}degree Celsius.\n The atmosphere there is {atm}.\n The wind speed is {wind} kilometer per hour" \
           f"\n This data is last updated at {time}")

print(data_say)                                                   # output text
speak.Speak(data_say)                                             # output text to speech

