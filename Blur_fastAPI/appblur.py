from flask import *
import os
import numpy as np
import cv2
from pdf2image import convert_from_path

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "static/"

@app.route('/url', methods=['POST'])
def pdf():
    if request.method == "POST":
        image = request.files["image"]
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
        filename = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
        print("stored as:" + filename)
        pages = convert_from_path(filename,520,poppler_path=r'C:\Users\User\Documents\GitHub\poppler-0.68.0\bin')
        for i in range(len(pages)):
            pages[i].save('./static/image.jpg', 'JPEG')
            break
        filename = 'static/image.jpg'
        return redirect(url_for('.image', filename=filename))
    return "method not POST"

@app.route('/image', methods=['POST','GET'])
def image():
    #image blur 
    image = request.args['filename'] 
    img = cv2.imread(image)
    blurred_img = cv2.GaussianBlur(img,(33,33),300)
    mask = np.zeros((6074,4290,3), 'uint8')
    mask = cv2.rectangle(mask, (4000,2000), (100,3200), (255, 255, 255),-1)
    out = np.where(mask==np.array([255, 255, 255]), img, blurred_img)
    cv2.imwrite("./static/Blur.jpg", out)
    path = "static/blur.jpg"
    return render_template("pdfsave.html" , path = path)


@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return("Woops,Page Not Found, that page doesnot exist on your path!")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7000, debug=True)