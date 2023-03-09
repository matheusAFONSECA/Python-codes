import os
import glob
from PIL.Image import FASTOCTREE
from sklearn.model_selection import train_test_split
import shutil
from my_utils import split_data, order_test_set, create_generators

from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import tensorflow as tf

from deeplearning_model import streesings_model

# this code is for us run some examples of paths and folders from de datasets
if __name__ == "__main__":
    x = True

    if not x:  # this is for we use other functions as examples
        path_to_data = "C:\\Users\\mathe\\Downloads\\archive\\Train"  # the index of the path train
        path_to_save_train = "C:\\Users\\mathe\\Downloads\\archive\\training_data\\train"  # where we want to save our training
        path_to_save_val = "C:\\Users\\mathe\\Downloads\\archive\\training_data\\val"  # where we want to save our validation
        split_data(path_to_data, path_to_save_train=path_to_save_train, path_to_save_val=path_to_save_val)

    if not x:
        path_to_images = "C:\\Users\\mathe\\Downloads\\archive\\Test"  # the path of tests
        path_to_csv = "C:\\Users\\mathe\\Downloads\\archive\\Test.csv"  # the path cvs file of tests
        order_test_set(path_to_images, path_to_csv)  # function which can order the dataset

    path_to_train = "C:\\Users\\mathe\\Downloads\\archive\\training_data\\train"  # where we want to save our training
    path_to_val = "C:\\Users\\mathe\\Downloads\\archive\\training_data\\val"  # where we want to save our validation
    path_to_test = "C:\\Users\\mathe\\Downloads\\archive\\Test"
    batch_size = 64
    epochs = 15
    lr = 0.0001  # learning rate

    train_genarator, val_genarator, test_genarator = create_generators(batch_size, path_to_train, path_to_val,
                                                                       path_to_test)
    nbr_clases = train_genarator.num_classes

    TRAIN = False  # when we want to train we turn it to TRUE

    TEST = True  # when we want to stop to test we turn it to FALSE

    if TRAIN:
        path_to_save_model = './Model'
        ckpt_saver = ModelCheckpoint(
            path_to_save_model,
            monitor="val_accuracy",
            mode='max',
            save_best_only=True,
            save_freq='epoch',
            verbose=1
        )

        early_stop = EarlyStopping(monitor="val_accuracy", patience=10)

        model = streesings_model(nbr_clases)

        optmizer = tf.keras.optmizers.Adam(learning_rate=lr, amsgrad=True)

        model.compile(optimizer=optmizer, loss='categorical_crossentropy', metrics=['accuracy'])

        model.fit(train_genarator,
                  epochs=epochs,
                  batch_size=batch_size,
                  validation_data=val_genarator,
                  callbacks=[ckpt_saver, early_stop]
                  )

    if TEST:
        model = tf.keras.models.load_model('./Model')
        model.summary()

        print("Evaluating validation set:")
        model.evaluate(val_genarator)

        print("Evaluatin test set:")
        model.evaluate(test_genarator)
