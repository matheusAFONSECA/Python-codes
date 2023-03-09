import cv2
import pytesseract

img = cv2.imread('C:\\Users\\mathe\\Downloads\\archive\\imagens\\Images\\d019df2153f04c8a0a1dd990e2706091.jpg')

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\Tesseract.exe"

# Adding custom options
custom_config = r'--oem 3 --psm 6'
resultado = pytesseract.image_to_string(img, config=custom_config)

print(resultado)
