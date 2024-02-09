import cv2
import numpy as np
from gcci1 import *
from app import get_date
from datetime import date
import importlib , os , uuid
from pdf2image import convert_from_path
def detect_row_segments(image):
    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    _, labels, stats, _ = cv2.connectedComponentsWithStats(binary_image)

    min_area_threshold = 58
    large_regions = [label for label, stat in enumerate(stats[1:], start=1) if stat[4] > min_area_threshold]
    large_regions = sorted(large_regions, key=lambda label: stats[label][1])

    row_segments = []
    current_row = []
    prev_bottom = -1

    for label in large_regions:
        x, y, width, height, _ = stats[label]

        # # Exclude segments with width > 1400 and height > 200
        # if width <= 1400 and height <= 200:
        # Check if it belongs to a new row based on vertical distance
        if prev_bottom != -1 and y - prev_bottom > 22:
            row_segments.append(current_row)
            current_row = []

        current_row.append((x, y, width, height))
        prev_bottom = y + height

    # Remove the first two segments and the last segment
    if len(row_segments) > 2:
        row_segments = row_segments[2:-1]
    else:
        row_segments = []

    segmented_rows = []
    for row in row_segments:
        row_x, row_y, row_width, row_height = zip(*row)
        min_x = min(row_x)
        max_x = max(row_x) + max(row_width)
        min_y = min(row_y)
        max_y = max(row_y) + max(row_height)
        row_image = image[min_y:max_y, min_x:max_x]
        segmented_rows.append(row_image)

    for j, segment in enumerate(segmented_rows, 1):
        cv2.imwrite(f'segment_{j}.png', segment)

    return len(segmented_rows)

def convert_pdf_to_images(pdf_path, output_path):
    images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    print(len(images))
    path=get_date()
    # Save the modified DataFrame back to Excel
    path_1 = path[0].replace('.pdf','.xlsx')
    for i, image in enumerate(images):
        image_path = f"{output_path}/page_{i+1}.png"
        image.save(image_path, "PNG")

        # detecting and splitting Single Image
        number_of_segments = detect_row_segments(image_path)
        print(f"No of Segments Found in image-{i} is : {number_of_segments}")

        for k in range(1,number_of_segments+1):

            cut_image(f"segment_{k}.png")
            subImg_2_excel(path_1)
            os.remove(f"segment_{k}.png")
        print(f"Page {i+1} saved as {image_path}")
    print(path_1)
    os.remove("left_side.jpg")
    os.remove("right_side.jpg")
    return [path_1]

def convert():
    path = get_date()
    print(path)
    file = path[0]
    today = date.today()
    print("Today's date:", today)
    r_filename = str(uuid.uuid4())
    pa_th = os.path.join(os.getcwd(),'static',str(today) , r_filename)
    os.makedirs(pa_th, exist_ok=True)
    pdf_file = file
    output_directory = pa_th
    # This code will only execute if the script is run directly, not when imported
    return convert_pdf_to_images(pdf_file, output_directory)