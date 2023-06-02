import os
from PIL import Image
import pytesseract

# Adding custom options for pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\Tesseract.exe"
custom_config = r'--oem 3 --psm 6'

# Define o diretório da pasta de imagens
pasta_imagens = "C:\\Users\\mathe\\Downloads\\placas"

# Lista os arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Percorre cada arquivo na pasta
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem
    if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
        # Abre a imagem
        caminho_imagem = os.path.join(pasta_imagens, arquivo)
        imagem = Image.open(caminho_imagem)

        # Realiza o OCR na imagem
        resultado = pytesseract.image_to_string(imagem, config=custom_config)

        # Imprime o texto encontrado na imagem
        print(f"Arquivo: {arquivo}")
        print(f"Texto: {resultado}")
        print("-" * 20)
