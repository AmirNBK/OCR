from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_recognition(filename='images.png', output_file='output_text.txt' , language="fas"):
    img = Image.open(filename)
    text = pytesseract.image_to_string(img,language)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

ocr_recognition('images.png', 'output_text.txt' , 'fas')