def dotProduct(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")

    total = 0

    for i in range(len(v1)):
        total += v1[i] * v2[i]

    return total


class Perceptron:
    def __init__(self, weights, threshold):

        self.n = len(weights)
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        if len(inputs) != self.n:
            raise ValueError("Incorrect number of inputs")

        value = dotProduct(inputs, self.weights)

        return value >= self.threshold


def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def gradient(f, point, h=1e-5):
    grad = []

    for i in range(len(point)):
        shifted = point.copy()
        shifted[i] += h

        partial = (f(*shifted) - f(*point)) / h
        grad.append(partial)

    return grad


v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(dotProduct(v1, v2))


p = Perceptron(
    weights=[0.5, -1, 2],
    threshold=1
)

print(p.predict([1, 2, 3]))


def f(x):
    # f(x) = x^2
    return x**2


print(derivative(f, 3))


def g(x, y, z):
    return x**2 + y*z


print(gradient(g, [1, 2, 3]))