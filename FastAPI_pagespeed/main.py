from fastapi import *
import importlib
from fastapi.responses import *
app = FastAPI()
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


@app.post('/url')
def pdf(request: Request,url: str = Form(...)):
    print(url,"pdf route")
    from desktoppage import desktop
    pdf = desktop()
    from mobilepage import mobile
    pdf2 = mobile()
    return templates.TemplateResponse("pdfsave.html", {"request": request,"pdf":pdf,"pdf2":pdf2})
    
def upload_file(url: str = Form(...)):
    print(url,"main.py")
    return url

@app.get('/')
def index(request: Request):
    try:
        # return templates.TemplateResponse("item.html", {"request": request, "id": id}
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return("Woops,Page Not Found, that page doesnot exist on your path!")
