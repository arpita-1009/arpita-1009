from fastapi import *
import os , shutil , cv2
import numpy as np
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from pdf2image import convert_from_path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post('/url')
def pdf(request: Request , file: UploadFile = File(...)):
    filename = os.path.join("./static", file.filename)
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    pages = convert_from_path(filename,520,poppler_path=r'C:\Users\User\Documents\GitHub\poppler-0.68.0\bin')
    for i in range(len(pages)):
        pages[i].save('./static/image.jpg', 'JPEG')
        break
    filename = 'static/image.jpg'
    
    return templates.TemplateResponse("sam.html", {"request": request , "filename":filename})

@app.post('/image')
def image(request: Request,filename: str = Form(...)):
    image = filename
    print(filename , "*************",image ,"filepath******************************************")
    img = cv2.imread(image)
    blurred_img = cv2.GaussianBlur(img,(33,33),300)
    mask = np.zeros((6074,4290,3), 'uint8')
    mask = cv2.rectangle(mask, (4000,2000), (100,3200), (255, 255, 255),-1)
    out = np.where(mask==np.array([255, 255, 255]), img, blurred_img)
    cv2.imwrite("./static/Blur.jpg", out)
    path = "./static/blur.jpg"


    return templates.TemplateResponse("pdfsave.html", {"request": request , "path":path})

@app.get('/')
def index(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        return("Woops,Page Not Found, that page doesnot exist on your path!")