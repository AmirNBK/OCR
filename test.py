from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_recognition(filename='photo.jpg', output_file='output_text.txt' , language="fas"):
    img = Image.open(filename)
    text = pytesseract.image_to_string(img,language)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

# Call the ocr_recognition function with the filename of your image and the output file path
ocr_recognition('photo.jpg', 'output_text.txt' , 'fas')


# # Timeout/terminate the tesseract job after a period of time
# try:
#     print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
#     print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
#     # Tesseract processing is terminated
#     pass

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('photo.jpg')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('photo.jpg')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('photo.jpg')))

# # Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('photo.jpg', extension='pdf')
# with open('test.pdf', 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default

# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('photo.jpg', extension='hocr')

# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('photo.jpg')