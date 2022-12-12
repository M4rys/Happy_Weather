from fastapi import APIRouter, Form, Request
from repositories import Repositories
from scheama import RequestDataCity, Forecast
from fastapi.templating import Jinja2Templates

router = APIRouter()# instacia da classe fastaAPI
templates = Jinja2Templates(directory="templates")
    
@router.get("/ByCity/By_City")
def go_to_City_search(request: Request):
    return templates.TemplateResponse("ByCity/By_city.html",{"request": request, "message": ""})

@router.post("/submitForm")
async def handle_form(request: Request,  State: str= Form(...), City: str= Form(...)):
    requesta = RequestDataCity(City= City, State=State)
    global data
    data = Repositories.Find_By_City(requesta)
    if data == None:
        return templates.TemplateResponse("ByCity/By_city.html",{"request": request, "message": "Não foi encontrado a cidade, confira se os dados fornecidos estão corretos."})
    else:
        ThisDay, Forecasts1, Forecasts2 = Repositories.Next_Days(data["results"]["forecast"])

    return templates.TemplateResponse("Results/Results_heather.html",{"request": request, "Temp": data["results"]["temp"],
                                        "Wind_speedy":data["results"]["wind_speedy"], "Humidity": data["results"]["humidity"],
                                        "City": data["results"]["city"],"ThisDay": ThisDay ,"forecasts":Forecasts1, "forecasts2": Forecasts2})
