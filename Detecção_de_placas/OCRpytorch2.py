import torch
from torchvision import transforms
from torchvision.transforms import functional as F
from PIL import Image
from torchvision.models import resnet50
from torchvision_transformers import OCRTransformer

# Load the pre-trained ResNet50 model
model = resnet50(pretrained=True)

# Load the OCR transformer
ocr_transformer = OCRTransformer(model)

def read_text_from_image(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Preprocess the image
    image = F.to_tensor(image)
    image = F.normalize(image, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    image = image.unsqueeze(0)

    # Perform OCR using the OCR transformer
    predictions = ocr_transformer(image)
    text = ''.join(predictions[0]["text"])

    return text

# Path to the image file
image_path = "D:\\Downloads\IDENTIFICACAO DE PLACAS\\RESULTADOS_OCR_YOLO_IDENTIFICACAO_CARACTERES\\300 imagens\\placas\\7f56adf4b9306ac9_jpg.rf.fcfb606af4d29de723e219ec05e5b9c9_1_0.jpg"

# Call the function to read text from the image
result = read_text_from_image(image_path)

# Print the extracted text
print(result)
