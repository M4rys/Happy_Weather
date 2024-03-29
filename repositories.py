# Importando as bibliotecas necessárias
import requests
import json
import os
from scheama import ResponseData, Forecast

# Classe que cria as funções necessárias para o funcionamento da página

class Repositories:
    
    # Função que devolve os dados referentes a solicitação referentes por meio da base da API
    
    def CriaJsonWithAPIData(webpath):
        response_API = requests.get(webpath)
        new_data = response_API.text
        response_API.close()
        new_data = json.loads(new_data)
        return new_data

    # Função que a partir do IP do usuário, obtém as informações 
    def Find_By_IP(ip): # gets the information from the API base on the user IP 
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&user_ip={}".format(ip)
        API_Data = Repositories.CriaJsonWithAPIData(path)
        return API_Data
        
    # Função que obtém as informações da base da API sobre a cidade que o usuário escolheu
    
    def Find_By_City(local): 
        city = local.City.capitalize()
        state = local.State.upper()
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name={},{}".format(city, state)
        API_Data = Repositories.CriaJsonWithAPIData(path)
        print(city.upper(), "==" ,API_Data["results"]["city"].split(",")[0].upper())
        if city.upper() == API_Data["results"]["city"].split(",")[0].upper():
            return API_Data
        else: 
            return None
        
    # Função que realiza o processamento das informações referentes ao clima para serem retornadas ao usuário final
    
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
                
        # A variável ThisDay contém a informação referente ao dia atual 
        
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

