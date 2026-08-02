import mnist_loader
import random
import numpy as np


# Goal: Create a classifier that determines if a digit is 0 using a single neuron
# Goal: Make the code I wrote follow the patterns set in find_m_and_b.py

# def derivative(f, x, h=1e-5):
#     return (f(x + h) - f(x)) / h


def gradient(f, point, h=1e-5):
    grad = np.zeros_like(point)

    for i in range(len(point)):
        shifted = point.copy()
        shifted[i] += h

        grad[i] = (f(shifted) - f(point)) / h

    return grad


class ZeroDetector:

    def __init__(self):
        # First 784 values are weights
        # Last value is bias
        self.params = np.random.randn(785)

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def predict(self, x):

        weights = self.params[:784]
        bias = self.params[784]

        z = np.dot(weights, x) + bias

        return self.sigmoid(z)

    # Error as a function of the parameter vector
    def compute_error(self, params, x, target):

        weights = params[:784]
        bias = params[784]

        z = np.dot(weights, x) + bias

        a = self.sigmoid(z)

        return (a - target) ** 2

    # x is a picture, target is the output (1 if the picture is of a 0, 0 if it is a picture of a 1, 2, 3... or 9), learning_rate can range from 1 to 0.1
    def train_example(self, x, target, learning_rate):

        grad = gradient(
            lambda params: self.compute_error(
                params,
                x,
                target
            ),
            self.params
        )

        self.params -= learning_rate * grad

        return self.compute_error(
            self.params,
            x,
            target
        )

    def SGD(self, training_data, epochs, learning_rate):

        for epoch in range(epochs):

            random.shuffle(training_data)

            total_error = 0

            for x, digit in training_data:

                target = 1 if digit == 0 else 0

                total_error += self.train_example(
                    x,
                    target,
                    learning_rate
                )

            print(
                "Epoch:",
                epoch,
                "Error:",
                total_error
            )


training_data, validation_data, test_data = \
    mnist_loader.load_data()


training_pairs = list(zip(
    training_data[0],
    training_data[1]
))


detector = ZeroDetector()


detector.SGD(
    training_pairs,
    epochs=10,
    learning_rate=0.1
)


score = 0
elts_to_check = 1000


for i in range(elts_to_check):

    x = training_data[0][i]
    label = training_data[1][i]

    p = detector.predict(x)

    if label == 0:

        print("WE'VE GOT A 0")

        if p > .9:
            print("SUCCESSFUL PREDICTION!")
            score += 1

        else:
            print("FAILURE")
            score -= 1

    else:

        if p > .05:
            print("FAILURE")
            score -= 1

        else:
            print("SUCCESSFUL PREDICTION!")
            score += 1

    print("Probability of being a zero:", p * 100, "%")
    print("Actual digit:", label)


print(
    score / elts_to_check * 100,
    "%",
    "success rate"
)