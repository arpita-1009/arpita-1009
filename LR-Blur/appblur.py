from tkinter import Image
from flask import *
import os
import numpy as np
import importlib , cv2
from PIL import Image , ImageDraw , ImageFilter
from pdf2image import convert_from_path
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)
Image.MAX_IMAGE_PIXELS = None
app = Flask(__name__)

mappings = {
    'Gujarat712': ("guj_satb", "guj_satbara"),
    'GujaratProperty Card':("guj_prop","guj_propertycard"),
}

@app.route('/bluripvr', methods=['POST'])
def blur():
    if request.method =="GET":
        print("image pdf path if")
    if request.method == "POST":
        image = request.files["image"]
        # doc_type =request.form["type"]
        img = image.filename.strip(".pdf")
        doc_type =request.form["path"]
        path = doc_type.strip("/blur.jpg")
        print(path,"after strip poath")
        image.save(os.path.join(path, image.filename))

        filename = path +"/"+ image.filename
        print("stored blur pdf:" + filename)
        pages = convert_from_path(filename,520)
        for i in range(len(pages)):
            pages[i].save(path+'/image.jpg', 'JPEG')
            break
        im = Image.open(path +'/image.jpg')
        mask = Image.new('L', im.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle([ (4500,1000), (200,2300) ], fill=255)
        blurred = im.filter(ImageFilter.GaussianBlur(30))
        im.paste(blurred, mask=mask)
        im.save(path +"/"+"blurredImg.jpg")
        # 2nd part blur*********************************
        im = Image.open(path +"/"+'blurredImg.jpg')
        mask = Image.new('L', im.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle([ (2000,4000), (1600,4300) ], fill=255)
        blurred = im.filter(ImageFilter.GaussianBlur(30))
        im.paste(blurred, mask=mask)
        im.save(path +"/"+"12.jpg")
        im = Image.open(path +"/"+"12.jpg")
        mask = Image.new('L', im.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle([ (4000,4300), (300,5000) ], fill=255)
        blurred = im.filter(ImageFilter.GaussianBlur(30))
        im.paste(blurred, mask=mask)
        im.save(path +"/"+"12.jpg")
        path = path+"/12.jpg"

        return render_template("712.html" , path = path)

@app.route('/url', methods=['POST'])

def pdf():
    if request.method == "POST":
        image = request.files["image"]
        doc_type =request.form["type"]
        img = image.filename.strip(".pdf")
        path = "static/"+img
        if os.path.exists(path) == True:
                pass
        else:
            os.mkdir(path)
        image.save(os.path.join(path, image.filename))
        filename = os.path.join(path, image.filename)
        print("stored as:" + filename)
        pages = convert_from_path(filename,520)
        for i in range(len(pages)):
            pages[i].save(path+'/image.jpg', 'JPEG')
            break

        filename1 = path+'/image.jpg'
        # filename1 = filename1.strip("./")
        print(filename1,"filename 1")
        return redirect(url_for('.image', filename1 = filename1 ,path = path, filename=filename, doc_type=doc_type))
    return " method not POST "

@app.route('/image', methods=['POST','GET'])
def image():
    image = request.args['filename1'] 
    print(image)
    path = request.args['path']
    doc_type = request.args['doc_type']
    print(path,"path in image function")

    img = cv2.imread(image)
    blurred_img = cv2.GaussianBlur(img,(33,33),300)
    mask = np.zeros((6074,4290,3) , 'uint8')
    mask = cv2.rectangle(mask, (4000,2000), (100,3300), (255, 255, 255),-1)
    out = np.where(mask==np.array([255, 255, 255]), img, blurred_img)
    cv2.imwrite(path+"/Blur.jpg", out)
    path = path+"/blur.jpg"
    import datetime
    x = datetime.datetime.now()
    date = x.strftime("%d %B %Y")
    num = "Gujarat"
    if doc_type == "8A":
        return render_template("8A.html",path = path)
    elif doc_type == "712":
        pyfile, func= mappings[num + doc_type]
        module = importlib.util.find_spec(pyfile, package=None)
        m = module.loader.load_module()
        function = getattr(m, func)
        owner = function()
        print(owner)
        return render_template("712index.html" , path = path ,owner = owner,date = date)
    else:
        pyfile, func= mappings[num + doc_type]
        module = importlib.util.find_spec(pyfile, package=None)
        m = module.loader.load_module()
        function = getattr(m, func)
        owner = function()
        print(owner)
        
        return render_template("propindex.html" , path = path ,owner = owner,date = date)
        
def getimage():
    filename = request.args['filename'] 
    return filename

@app.route('/reload', methods=['POST','GET'])
def delete():
    doc_type =request.form["path"]
    # print(doc_type,"doc_type************8")
    path = doc_type.strip("/blur.jpg")
    print(path,"after strip poath")
    # import shutil
    # try:
    #     shutil.rmtree(path)
    # except:
    #     print("file is not delete")
    
    return render_template("bluripvr.html", path =path )


@app.route('/delete', methods=['POST','GET'])
def del1():
    doc_type =request.form["path"]
    print(doc_type,"doc_type************8")
    path = doc_type.strip("/12.jpg")
    print(path,"after strip poath")
    import shutil
    try:
        # shutil.rmtree(path)
        print("osijdicuhdsu")
    except:
        print("file is not delete")
    
    return "DONE"

@app.route('/')
def home():
    try:
        return render_template('mainindex.html')
    except Exception as e:
        return("Woops,Page Not Found, that page doesnot exist on your path!")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7000, debug=True)