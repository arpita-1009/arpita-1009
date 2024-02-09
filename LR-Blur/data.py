import os

# importing flasks
from flask import Flask, render_template, request

import cv2

# to check and secure filename entered by user , "NEVER TRUST USER ENTERED DATA"
from werkzeug.utils import secure_filename

# module for converting pdf to image and make changes
from pdf2image import convert_from_path

from PIL import Image, ImageFilter
import pytesseract

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, 'static')


@app.route('/')
def index():
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_name = secure_filename(file.filename)
        print(file_name,"******")
        file.save(file_name)
        fname = file.filename
        path = f'{fname}'
        img_file = path.replace(".pdf", "")

        images = convert_from_path(path, poppler_path=r'C:\Users\Arpita Patel\Documents\GitHub\poppler-0.68.0\bin')

        count = 0
        for page in range(len(images)):
            count += 1
            # jpeg_file = img_file + str(count) + ".jpeg"
            # images[page].save(os.path.join(
            #     app.root_path, UPLOAD_FOLDER, 'pages', jpeg_file))

            path_to_tesseract = r"C:\Users\Arpita Patel\AppData\Local\Tesseract-OCR\tesseract.exe"
            image_path = os.path.join(
                UPLOAD_FOLDER + '\pages', img_file+str(count) + ".jpeg")

            main_image = Image.open('static/12.png')
            pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            cordinate = (x1, y1, x2, 0)

            img = cv2.imread('static/12.png')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Detecting Words
            # hImg, wImg, _ = img.shape
            boxes = pytesseract.image_to_data(img, lang="eng+guj")
            print(boxes)
            # code to make boxes around every workds
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            for x, b in enumerate(boxes.splitlines()):
                if x != 0:
                    b = b.split()

                    if len(b) == 12:
                        x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                        # cv2.rectangle(
                        #     img, (x, y), (w + x, h + y), (0, 0, 255), 1)
                        # print(b[11])
                        # if "Survey/" in b[11]:
                        #     x1, y1, x2, y2 = b[6] , b[7] , b[8] , b[9]
                        #     upp_cor = (x1, y1)
                        #     print("Survey Cordinates",upp_cor)
                        if "Survey/" in b[11]:
                            x1, y1 = b[6], b[7]
                            print("Upper Coordinates : ", x1, y1)

                        elif "(રીમાર્ક્સ)" in b[11]:
                            print("ushchsdkjchsdhhkj")
                            x2, y2 = b[8], b[9]
                            print("Lower Coordinates : ", x2, y2)
                     

                        cordinate = x1, y1, x2, y2
                        print("COORDINATES ARE HERE : ", cordinate)

                cropped_image = main_image.crop(cordinate)
                blurred_image = cropped_image.filter(
                    ImageFilter.GaussianBlur(radius=3))
                main_image.paste(blurred_image, (cordinate))
                # main_image.show()
        return 'file uploaded successfully'
if __name__ == '__main__':
    app.run(debug=True)


