from pdf2image import convert_from_path
import pytesseract
import util
from prescription_parser import prescriptionparser
from patient_parser import patientdetailparser
POPPLER_PATH = r"C:\poppler-23.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extractor(file_path , file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document = ''
    if len(pages)>0:
        page = pages[0]
        process_img = util.processing_image(page)
        text = pytesseract.image_to_string(process_img, lang="eng")
        document = "\n" + text


    if file_format=="prescription":
        extracted_data = prescriptionparser(document).parse()
    elif file_format=="patient_details":
        extracted_data = patientdetailparser(document).parse()
    else :
        raise Exception(f"Invalid file format {file_format}")
    return extracted_data
if __name__ == "__main__":
    details=extractor('../resources/prescription/pre_1.pdf' ,"prescription")
    print(details)



