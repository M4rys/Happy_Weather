import requests
import json
import os
from scheama import ResponseData, Forecast

class Repositories:

    def CriaJsonWithAPIData(webpath):
        response_API = requests.get(webpath)
        new_data = response_API.text
        response_API.close()
        new_data = json.loads(new_data)
        return new_data


    def Find_By_IP(): # gets the information from the API base on the user IP 
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&user_ip=remote"
        API_Data = Repositories.CriaJsonWithAPIData(path)
        return API_Data
        

    def Find_By_City(local): # gets the information from the API base on the city the user chose
        city = local.City.capitalize()
        state = local.State.upper()
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name={},{}".format(city, state)
        API_Data = Repositories.CriaJsonWithAPIData(path)
        print(city.upper(), "==" ,API_Data["results"]["city"].split(",")[0].upper())
        if city.upper() == API_Data["results"]["city"].split(",")[0].upper():
            return API_Data
        else: 
            return None
    def Next_Days(forecastData):
        Forecasts2 = []
        for i in forecastData:
            if i["description"] == "Parcialmente nublado":
                Forecasts2.append(Forecast(date = i["date"],
                                                weekday = i["weekday"],
                                                max = i["max"],
                                                min = i["min"],
                                                cloudiness = i["cloudiness"],
                                                rain = i["rain"],
                                                rain_probability = i["rain_probability"],
                                                wind_speedy = i["wind_speedy"],
                                                description = "Parc. nublado",
                                                condition = i["condition"]))
            else:
                Forecasts2.append(Forecast(date = i["date"],
                                                weekday = i["weekday"],
                                                max = i["max"],
                                                min = i["min"],
                                                cloudiness = i["cloudiness"],
                                                rain = i["rain"],
                                                rain_probability = i["rain_probability"],
                                                wind_speedy = i["wind_speedy"],
                                                description = i["description"],
                                                condition = i["condition"]))
        ThisDay = Forecasts2[0]
        del Forecasts2[0]
        Forecasts1 = []
        for _ in range(0,4):
            Forecasts1.append(Forecasts2[0])
            del Forecasts2[0]
        del Forecasts2[len(Forecasts2)-1]
        return ThisDay, Forecasts1, Forecasts2

    # def login():
    #     pass


Repositories.Find_By_IP()
