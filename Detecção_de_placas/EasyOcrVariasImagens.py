import os
from PIL import Image
import easyocr


def read_text_from_image(image_path):
    # Create an OCR reader using the desired language(s)
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(image_path)

    # Extract the text from the OCR result
    text = ' '.join([res[1] for res in result])

    return text


# Define o diretório da pasta de imagens
pasta_imagens = "D:\\Downloads\\IDENTIFICACAO DE PLACAS\\RESULTADOS_OCR_YOLO_IDENTIFICACAO_CARACTERES\\300 imagens\\placas"

# Lista os arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Percorre cada arquivo na pasta
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem
    if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
        # Abre a imagem
        caminho_imagem = os.path.join(pasta_imagens, arquivo)
        imagem = Image.open(caminho_imagem)

        # chama a funcao que irá ler o texto da imagem
        resultado = read_text_from_image(imagem)

        # Imprime o texto encontrado na imagem
        print(f"Arquivo: {arquivo}")
        print(f"Texto: {resultado}")
        print("-" * 20)
