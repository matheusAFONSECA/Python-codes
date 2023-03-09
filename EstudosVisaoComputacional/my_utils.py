import matplotlib.pyplot as plt
import numpy as np
import shutil
import os
from sklearn.model_selection import train_test_split
import glob
import csv
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def display_some_examples(examples, labels):  # a function to help us how to use images in the datacenter
    # it will generate diffent images
    plt.figure(figsize=(10, 10))

    for i in range(25):
        idx = np.random.randint(0, examples.shape[0] - 1)  # this is used to get a image from x_train/y_train
        img = examples[idx]
        label = labels[idx]

        plt.subplot(5, 5, i + 1)  # plot the images
        plt.title(str(label))  # title for each image
        plt.tight_layout()
        plt.imshow(img, cmap='gray')

    plt.show()  # this says to the code to show all the figure at the end of the for


def split_data(path_to_data, path_to_save_train, path_to_save_val, split_size=0.1):
    # function that acess the paths and make them in data
    # splt size = 0.1, so 90% training and 10% validation

    folders = os.listdir(path_to_data)  # return the list of the folders in that path

    for folder in folders:

        full_path = os.path.join(path_to_data, folder)
        image_paths = glob.glob(os.path.join(full_path, '*.png'))  # define the type of folders which we want

        x_train, x_val = train_test_split(image_paths, test_size=split_size)

        for x in x_train:

            path_to_folder = os.path.join(path_to_save_train, folder)

            if not os.path.isdir(path_to_folder):  # if the path doens't exist, it will create one
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)

        for x in x_val:

            path_to_folder = os.path.join(path_to_save_val, folder)

            if not os.path.isdir(path_to_folder):  # if the path doens't exist, it will create one
                os.makedirs(path_to_folder)

            shutil.copy(x, path_to_folder)


def order_test_set(path_to_images, path_to_csv):

    try:
        with open(path_to_csv, 'r') as csvfile:

            reader = csv.reader(csvfile, delimiter=',')

            for i, row in enumerate(reader):

                if i == 0:
                    continue

                img_name = row[-1].replace('Test/', '')  # without this we there can be a ERROR in our code because of csv
                label = row[-2]

                path_to_folder = os.path.join(path_to_images, label)

                if not os.path.isdir(path_to_folder):
                    os.makedirs(path_to_folder)

                img_full_path = os.path.join(path_to_images, img_name)
                shutil.move(img_full_path, path_to_folder)

    except:
        print('[INFO] : Error reading csv file')


def create_generators(batch_size, train_data_path, val_data_path, test_data_path):

    train_preprocessor = ImageDataGenerator(   # var which porcess the data before we use the deeplearnin model
        rescale=1/255.,  # rescale the images
        rotation_rage=10,
        width_shift_range=0.1
    )

    test_preprocessor = ImageDataGenerator(  # var which porcess the data before we use the deeplearnin model
        rescale=1 / 255.,  # rescale the images
    )

    train_genarator = train_preprocessor.flow_from_directory(
        train_data_path,
        class_mode="categorical",
        target_size=(60, 60),  # convet the images into 60X60
        color_mode='rgb',
        shuffle=True,
        batch_size=batch_size
    )

    val_genarator = test_preprocessor.flow_from_directory(
        val_data_path,
        class_mode="categorical",
        target_size=(60, 60),  # convet the images into 60X60
        color_mode='rgb',
        shuffle=True,
        batch_size=batch_size
    )

    test_genarator = test_preprocessor.flow_from_directory(
        test_data_path,
        class_mode="categorical",
        target_size=(60, 60),  # convet the images into 60X60
        color_mode='rgb',
        shuffle=True,
        batch_size=batch_size
    )

    return train_genarator, val_genarator, test_genarator
