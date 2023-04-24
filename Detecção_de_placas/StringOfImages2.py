import os
import cv2
import pytesseract
from PIL import Image

# pasta com imagens
image_folder = "teste"

# pasta para salvar as placas recortadas
output_folder = os.path.join(os.path.expanduser("~"), "Downloads", "placas")
os.makedirs(output_folder, exist_ok=True)

# arquivo para salvar as strings capturadas
output_file = os.path.join(os.path.expanduser("~"), "Downloads", "strings_placas.txt")

# caminho para o arquivo de treinamento com os labels
labels_path = "labels/"

# carrega o arquivo com os nomes das classes
class_names = []
with open(os.path.join(labels_path, "classes.txt"), "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# percorre todos os arquivos de texto na pasta de labels
for txt_file in os.listdir(labels_path):
    if txt_file.endswith(".txt"):
        # abre o arquivo e lê as linhas
        with open(os.path.join(labels_path, txt_file), "r") as f:
            lines = f.readlines()

        # percorre todas as linhas no arquivo de texto
        for line in lines:
            # separa as informações em uma lista
            line_info = line.strip().split()

            # a primeira coluna é o nome da classe
            class_idx = int(line_info[0])

            # as colunas 2 a 5 são as coordenadas da caixa delimitadora
            x1, y1, x2, y2 = [int(coord) for coord in line_info[1:]]

            # carrega a imagem correspondente
            img_file = os.path.join(image_folder, txt_file.replace(".txt", ".jpg"))
            img = cv2.imread(img_file)

            # recorta a imagem usando as coordenadas da caixa delimitadora
            cropped = img[y1:y2, x1:x2]

            # salva a imagem recortada
            output_file_path = os.path.join(output_folder, f"{txt_file.replace('.txt', '')}_{class_names[class_idx]}.jpg")
            cv2.imwrite(output_file_path, cropped)

            # aplica OCR na imagem recortada
            im_pil = Image.fromarray(cropped)
            text = pytesseract.image_to_string(im_pil, lang='eng', config='--psm 6')

            # adiciona a string capturada no arquivo de saída
            with open(output_file, "a") as f:
                f.write(f"{output_file_path}: {text}\n")
