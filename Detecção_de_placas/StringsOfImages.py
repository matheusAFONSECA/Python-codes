import os
import shutil
import cv2
import pytesseract
from pathlib import Path

# caminho do diretório de teste e arquivo com os labels
test_dir = 'teste'
label_file = 'labels.txt'

# criar diretório placas
placas_dir = str(Path.home() / 'Downloads' / 'placas')
os.makedirs(placas_dir, exist_ok=True)

# abrir arquivo de labels
with open(label_file) as f:
    labels = f.readlines()

# percorrer lista de labels
for label in labels:
    # separar nome do arquivo e coordenadas da placa
    parts = label.strip().split(' ')
    filename = parts[0]
    coords = [int(float(c)) for c in parts[1:]]

    # carregar imagem
    img_path = os.path.join(test_dir, filename)
    img = cv2.imread(img_path)

    # recortar placa
    x1, y1, x2, y2 = coords
    placa = img[y1:y2, x1:x2]

    # salvar placa em diretório placas
    filename = os.path.splitext(filename)[0] + '.jpg'
    cv2.imwrite(os.path.join(placas_dir, filename), placa)

# abrir arquivos de placas e aplicar OCR
with open('strings.txt', 'w') as f:
    for filename in os.listdir(placas_dir):
        if filename.endswith('.jpg'):
            # carregar imagem e aplicar OCR
            img_path = os.path.join(placas_dir, filename)
            img = cv2.imread(img_path)
            text = pytesseract.image_to_string(img)

            # salvar texto em arquivo strings.txt
            f.write(f'{filename}: {text}\n')
