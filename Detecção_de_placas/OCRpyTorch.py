import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models import resnet50

# Carregar o modelo pré-treinado
modelo = resnet50(pretrained=True)
modelo.eval()

# Carregar a imagem
imagem = Image.open('"D:\\Downloads\IDENTIFICACAO DE PLACAS\\RESULTADOS_OCR_YOLO_IDENTIFICACAO_CARACTERES\\300 imagens\\placas\\7f56adf4b9306ac9_jpg.rf.fcfb606af4d29de723e219ec05e5b9c9_1_0.jpg"')

# Pré-processamento da imagem
transformacao = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
imagem_processada = transformacao(imagem)
imagem_batch = torch.unsqueeze(imagem_processada, 0)

# Realizar inferência com o modelo
saida = modelo(imagem_batch)

# Imprimir o texto extraído
print(texto)
