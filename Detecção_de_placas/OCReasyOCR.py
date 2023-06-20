import easyocr

def read_text_from_image(image_path):
    # Create an OCR reader using the desired language(s)
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    result = reader.readtext(image_path)

    # Extract the text from the OCR result
    text = ' '.join([res[1] for res in result])

    return text

# Path to the image file
image_path = "D:\\Downloads\IDENTIFICACAO DE PLACAS\\RESULTADOS_OCR_YOLO_IDENTIFICACAO_CARACTERES\\300 imagens\\placas\\7f56adf4b9306ac9_jpg.rf.fcfb606af4d29de723e219ec05e5b9c9_1_0.jpg"

# Call the function to read text from the image
result = read_text_from_image(image_path)

# Print the extracted text
print(result)
