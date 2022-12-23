from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers.Get_By_City import router as Get_by_City
from routers.Get_By_IP import router as Get_by_IP

app = FastAPI()



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"], response_class= HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("Homepage.html",{"request": request})


@app.get("/pickWay/choice", response_class= HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("pickWay/choice.html",{"request": request})



app.include_router(Get_by_City)
app.include_router(Get_by_IP)