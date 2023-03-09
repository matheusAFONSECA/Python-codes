# code for us see how the machine learning give us a result based on what image we give to it
import numpy as np
import tensorflow as tf


def predict_with_model(model, imgpath):

    image = tf.io.read_file(imgpath)  # reading the image
    image = tf.image.decode_png(image, channels=3)  # decoding the images
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)  # convert bits to float32
    image = tf.image.resize(image, [60, 60])
    image = tf.expand_dims(image, axis=0)

    predictions = model.predict(image)
    predictions = np.argmax(predictions)

    return predictions


if __name__ == "__main__":

    img_path = "C:\\Users\\mathe\\Downloads\\archive\\Test\\8\\00697.png"
    img_path = "C:\\Users\\mathe\\Downloads\\archive\\Train\\0\\00000_00000_00018.png"

    model = tf.keras.models.load_model('./Model')
    prediction = predict_with_model(model, img_path)

    print(f"prediction = {prediction}")
