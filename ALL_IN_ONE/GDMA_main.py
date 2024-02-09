from PIL import Image
import cv2 , re
from GDMA1 import *
from app import get_date
from datetime import date
import importlib , os , uuid



def cut_image(image_path):

    # Open the image file
    image = Image.open(image_path)

    # Crop the image from the top
    cropped_image = image.crop((0, 218, image.width, image.height))

    # Save the cropped image to the current directory
    cropped_image.save(image_path)

    # Close the image file
    image.close()

    # Load the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    middle_x_coordinate = int(width/2)
    # Define the starting x-coordinate for cropping
    # start_x = 633
    start_x = middle_x_coordinate

    # Crop the right and left sides of the image
    right_side = image[:, start_x:]
    left_side = image[:, :start_x]

    # Save the right and left side images
    cv2.imwrite("right_side.jpg", right_side)
    cv2.imwrite("left_side.jpg", left_side)


"----------------------------------------------------" \
"----------------------------------------------------"


from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_path):
    images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    print("Total Page Found : " , len(images))
    for i, image in enumerate(images):
        current_image_path = f"{output_path}\page_{i + 1}.jpg"
        image.save(current_image_path, "JPEG")
        scaling_factor = 300 / 96
        image = Image.open(current_image_path)
        # Calculate the new size of the image in pixels
        new_width = int(image.width * scaling_factor)
        new_height = int(image.height * scaling_factor)
        # Resize the image using the calculated size
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        # Set the new DPI information to 300 DPI
        resized_image.info["dpi"] = (300, 300)

        cut_image(current_image_path)
        full_page_text = extract_and_save_text_from_full_page()
        # print(full_page_text)

        # regex patterns to get strings like '51 ALCHEMIINDSTRUIES, 52 ALPAINDS'
        regex_pattern = r".*\d{2} [A-Z]{2}.*"

        # Use the findall method to extract strings matching the pattern
        splitting_list = re.findall(regex_pattern, full_page_text)

        # print(splitting_list)

        companies_data_list = get_company_data_list( full_page_text, splitting_list)
        filename =  f"GDMA_01_august.xlsx"
        for single_company_detail in companies_data_list:
            company_name,phone_numbers,email = extract_company_details(single_company_detail)
            add_data_to_excel(filename=filename,company_name=company_name,phone_numbers=phone_numbers,emails=email)
        os.remove(current_image_path)
    df = pd.read_excel(filename)

    # deleting row which have empty company name
    df = df[df.iloc[:, 0].apply(lambda x: pd.notnull(x) and len(str(x)) > 1)]
    path=get_date()
    # Save the modified DataFrame back to Excel
    path_1 = path[0].replace('.pdf','.xlsx')
    df.to_excel(path_1, filename, index=False)
    print("Excel Made Successfully")
    print(path_1)
    os.remove(filename)
    os.remove("left_side.jpg")
    os.remove("right_side.jpg")
    return [path_1]
# cut_image("1_pdf.png") # testing code


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