import cv2
import pytesseract

# Carregar a imagem com OpenCV
imagem = cv2.imread("D:\\Downloads\IDENTIFICACAO DE PLACAS\\RESULTADOS_OCR_YOLO_IDENTIFICACAO_CARACTERES\\300 imagens\\placas\\00447_jpg.rf.ffa7c8ad0374683f888dfa9a3a1ce78f_1_0.jpg")

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\Tesseract.exe"
custom_config = r'--oem 3 --psm 6'

# Converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar binarização
_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Realizar o OCR com Tesseract
texto = pytesseract.image_to_string(imagem_binaria)

# Imprimir o texto extraído
print(texto)
