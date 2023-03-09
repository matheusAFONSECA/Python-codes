import tensorflow  # used to deal to computer vision
import matplotlib.pyplot as plt  # used to create figures and adding images
import numpy as np
from tensorflow.keras.layers import Conv2D, Input, Dense, MaxPool2D, BatchNormalization, GlobalAvgPool2D
# the import above it's used to process images

"""
There three ways to create neural models:
-> tensorflow.keras.Sequencial = easiest way to create
-> functional approach = function that returns a model
-> tensorflow.keras.Model = inherit from this class
"""

# tensorflow.keras.Sequencial
seq_model = tensorflow.keras.Sequential(
    [
        Input(shape=(28, 28, 1)),  # it's the shape of our images
        Conv2D(32, (3, 3), activation='relu'),  # define the filters and the size of the
        Conv2D(64, (3, 3), activation='relu'),
        MaxPool2D(),
        BatchNormalization(),

        Conv2D(128, (3, 3), activation='relu'),
        MaxPool2D(),
        BatchNormalization(),

        GlobalAvgPool2D(),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')

    ]
)


# functional approach
def funcional_model():

    my_input = Input(shape=(28, 28, 1)),  # it's the shape of our images
    x = Conv2D(32, (3, 3), activation='relu')(my_input)  # define the filters and the size of the
    x = Conv2D(64, (3, 3), activation='relu')(x)
    x = MaxPool2D()(x)
    x = BatchNormalization()(x)

    x = Conv2D(128, (3, 3), activation='relu')(x)
    x = MaxPool2D()(x)
    x = BatchNormalization()(x)

    x = GlobalAvgPool2D()(x)
    x = Dense(64, activation='relu')(x)
    x = Dense(10, activation='softmax')(x)

    model = tensorflow.keras.Model(inputs=my_input, outputs=x)

    return model

# tensorflow.keras.Model
class MycutomModel(tensorflow.keras.Model):

    def __init__(self):
        super().__init__()

        self.conv1 = Conv2D(32, (3, 3), activation='relu')  # define the filters and the size of the
        self.conv2 = Conv2D(64, (3, 3), activation='relu')
        self.maxpool1 = MaxPool2D()
        self.batchnorm1 = BatchNormalization()

        self.conv3 = Conv2D(128, (3, 3), activation='relu')
        self.maxpool2 = MaxPool2D()
        self.batchnorm2 = BatchNormalization()

        self.globalavgpool1 = GlobalAvgPool2D()
        self.dense1 = Dense(64, activation='relu')
        self.dense2 = Dense(10, activation='softmax')

    def call(self, my_input):

        x = self.conv1(my_input)
        x = self.conv2(x)
        x = self.maxpool1(x)
        x = self.batchnorm1(x)
        x = self.conv3(x)
        x = self.maxpool2(x)
        x = self.batchnorm2(x)
        x = self.globalavgpool1(x)
        x = self.dense1(x)
        x = self.dense2(x)

        return x


def display_some_examples(examples, labels):  # a function to help us how to use images in the datacenter
    # it will generate diffent images
    plt.figure(figsize=(10, 10))

    for i in range(25):

        idx = np.random.randint(0, examples.shape[0]-1)  # this is used to get a image from x_train/y_train
        img = examples[idx]
        label = labels[idx]

        plt.subplot(5, 5, i+1)  # plot the images
        plt.title(str(label))  # title for each image
        plt.tight_layout()
        plt.imshow(img, cmap='gray')

    plt.show()  # this says to the code to show all the figure at the end of the for


if __name__ == '__main__':  # it's a good progaming habit to use this because it's separe behavior and imports

    (x_train, y_train), (x_test, y_test) = tensorflow.keras.datasets.mnist.load_data()

    """
    -> 'x_train' and 'y_train' are used to train our module
    -> 'x_test' and 'y_test' are used to test/validate our module 
    -> this will give us how well the neural is learning
    """

    print("x_train = ", x_train.shape)
    print("y_train = ", y_train.shape)
    print("x_test = ", x_test.shape)
    print("y_test = ", y_test.shape)

    """
    RESULTS: 
        x_train =  (60000, 28, 28)
        y_train =  (60000,)
        x_test =  (10000, 28, 28)
        y_test =  (10000,)
    """

    # display_some_examples(x_train, y_train)

    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    x_train = np.expand_dims(x_train, axis=-1)
    x_test = np.expand_dims(x_test, axis=-1)

    y_train = tensorflow.keras.utils.to_categorical(y_train, 10)
    y_test = tensorflow.keras.utils.to_categorical(y_test, 10)

    # compiling the model

    # model = funcional_model()
    model = MycutomModel()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

    # model training
    model.fit(x_train, y_train, batch_size=64, epochs=3, validation_split=0.2)

    # Evaluation on test set
    model.evaluate(x_test, y_test, batch_size=64)
