from fastapi import APIRouter, Request
from repositories import Repositories
from scheama import ResponseData, Forecast
from fastapi.templating import Jinja2Templates

router = APIRouter()# instacia da classe fastaAPI
templates = Jinja2Templates(directory="templates")



@router.get("/Results/Results_Weather/{ip}",  response_model= ResponseData, response_description="I found the Data ;)")
def get_data_Ip( request: Request, ip: str):
    
    data = Repositories.Find_By_IP(ip)
    ThisDay, Forecasts1, Forecasts2 = Repositories.Next_Days(data["results"]["forecast"])

    return templates.TemplateResponse("Results/Results_Weather.html",{"request": request, "Temp": data["results"]["temp"],
                                        "Wind_speedy":data["results"]["wind_speedy"], "Humidity": data["results"]["humidity"],
                                        "City": data["results"]["city"],"ThisDay": ThisDay ,"forecasts":Forecasts1, "forecasts2": Forecasts2})