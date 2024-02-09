import pandas as pd
import pytesseract , re
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M")


def extract_company_details(text):

    company_name_match = re.search(r'([A-Z\s.&.-]+)', text)
    company_name = company_name_match.group().strip() if company_name_match else None

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email = re.findall(email_pattern, text)

    '''---------'''
    pattern_10_digit = r"\d{3}[-\s]?\d{3}[-\s]?\d{4}"
    pattern_8_digit = r"\d{3}[-\s]?\d{3}[-\s]?\d{2}"

    phone_pattern = re.compile(r'''
\d{10}
                     
| \d{8}

| \b2\d{5}\b

| \d{3}-\d{7}  

| \d{4}-\d{7}

| \d{5}-\d{6}

| \d{5}-\d{7}

| \d{5}\s\d{5}

| \d{3}-\d{8}

| \d{4}-\d{8}

| \d{4}-\d{6}

| \d{3}-\d{6}
''', re.VERBOSE)
    phone_numbers = re.findall(phone_pattern, text)
    '''---------'''

    print("Phone Number(s) : " , phone_numbers)
    # print("Company Name : "  , company_name)
    # print("Email : "  , email , "\n\n\n")

    return company_name , phone_numbers , email

def extract_and_save_text_from_full_page():
    data = ""
    for img in ['left_side.jpg' , 'right_side.jpg']:
        ocr_text = pytesseract.image_to_string(img)
        data = data + ocr_text
    return data

def get_company_data_list(paragraph, company_list):
    company_details = []
    start_index = 0

    for i in range(len(company_list) - 1):
        current_company = company_list[i]
        next_company = company_list[i + 1]

        start_index = paragraph.find(current_company, start_index)
        end_index = paragraph.find(next_company, start_index)

        if start_index != -1 and end_index != -1:
            company_details.append(paragraph[start_index:end_index].strip())
        else:
            break

    # For the last company
    start_index = paragraph.find(company_list[-1], start_index)
    if start_index != -1:
        company_details.append(paragraph[start_index:].strip())

    return company_details


def add_data_to_excel(filename, company_name, phone_numbers, emails):
    data = {'Company Name': [], 'Phone Number': [], 'Email': []}

    max_length = max(len(phone_numbers), len(emails))
    phone_numbers += [''] * (max_length - len(phone_numbers))
    emails += [''] * (max_length - len(emails))

    for phone_number, email in zip(phone_numbers, emails):
        data['Company Name'].append(company_name)
        data['Phone Number'].append(phone_number)
        data['Email'].append(email)

    df = pd.DataFrame(data)

    try:
        existing_data = pd.read_excel(filename)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_excel(filename, index=False)


# full_page_text = extract_and_save_text_from_full_page()
# print(full_page_text)
#
# # regex patterns to get strings like '51 ALCHEMIINDSTRUIES, 52 ALPAINDS'
# regex_pattern = r".*\d{2} [A-Z]{2}.*"
#
# # Use the findall method to extract strings matching the pattern
# splitting_list = re.findall(regex_pattern, full_page_text)
#
# print(splitting_list)
#
# companies_data_list = get_company_data_list( full_page_text, splitting_list)
#
# for single_company_detail in companies_data_list:
#     company_name,phone_numbers,email = extract_company_details(single_company_detail)
#     filename =  f"GDMA_{datetime.now().strftime('%Y-%m-%d-%H-%M')}.xlsx"
#     add_data_to_excel(filename=filename,company_name=company_name,phone_numbers=phone_numbers,emails=email)

