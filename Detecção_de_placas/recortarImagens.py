import os
from PIL import Image

# define o diretório das imagens e labels
images_dir = "C:\\Users\\mathe\\Downloads\\teste"
labels_dir = "C:\\Users\\mathe\\Downloads\\labels"

# cria a pasta "placas" caso ela não exista
# if not os.path.exists('placas'):
#     os.makedirs('placas')

# percorre todas as imagens na pasta "images"
for image_filename in os.listdir(images_dir):
    # verifica se o arquivo é uma imagem
    if image_filename.endswith('.jpg') or image_filename.endswith('.png'):
        # carrega a imagem
        image_path = os.path.join(images_dir, image_filename)
        image = Image.open(image_path)

        # procura o arquivo de label correspondente
        label_filename = os.path.splitext(image_filename)[0] + '.txt'
        label_path = os.path.join(labels_dir, label_filename)

        # abre o arquivo de label e percorre cada linha
        bboxes = []
        with open(label_path, 'r') as f:
            for line in f:
                # extrai as coordenadas da caixa delimitadora
                values = line.strip().split(' ')
                x, y, w, h = map(float, values[1:])
                x1, y1 = int((x - w / 2) * image.width), int((y - h / 2) * image.height)
                x2, y2 = int((x + w / 2) * image.width), int((y + h / 2) * image.height)

                # adiciona a caixa delimitadora a uma lista
                bboxes.append((values[0], x1, y1, x2, y2))

        # ordena as caixas delimitadoras pela coordenada X do canto superior esquerdo
        bboxes = sorted(bboxes, key=lambda bbox: bbox[1])

        # recorta as imagens com base nas coordenadas ordenadas
        for i, bbox in enumerate(bboxes):
            class_id, x1, y1, x2, y2 = bbox
            cropped_image = image.crop((x1, y1, x2, y2))

            # salva a imagem recortada na pasta "placas"
            if class_id == "0":
                cropped_filename = f"{os.path.splitext(image_filename)[0]}_{i}_{class_id}.jpg"
                cropped_path = os.path.join("C:\\Users\\mathe\\Downloads\\placas", cropped_filename)
                cropped_image.save(cropped_path)
