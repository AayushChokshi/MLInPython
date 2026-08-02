import numpy as np
import random
import mnist_loader

class ZeroDetector:

    def __init__(self):
            self.weights = np.random.randn(784)
    
    def sigmoid(self, z):
        return 1.0/(1.0 + np.exp(-z))
    
    def predict(self, x):
          Z = np.dot(self.weights, x) + self.bias        
          return self.sigmoid(Z)
    
    def train_example(self, x, target, learning_rate):
          z = np.dot(self.weights, x) + self.bias
          a=self.sigmoid(z)
          delta = 2 * (a-target) * a * (1-a)
          grad_w = delta * x
          grad_b = delta
          self.weights -= grad_w*learning_rate
          self.bias -= grad_b * learning_rate
          return (a-target)**2
    


    def SGD(self, training_data, epochs, learning_rate):
          for epoch in range(epochs):
                random.shuffle(training_data)
                total_error = 0
                for x, digit in training_data:
                      target = 1 if digit ==0 else 0
                      total_error += self.train_example(
                            x,
                            target,
                            learning_rate
                      )

                    
                print(
                     "Epoch: " + epoch,
                     "Error : " + total_error
                )

training_data, validation_data, test_data = \
    mnist_loader.load_data()

print(len(training_data[0]))
print(len(training_data[1]))

x = training_data[0][0]
y = training_data[1][0]

print(x.shape)
print(y)


training_pairs = list(zip(
      training_data[0],
      training_data[1]


))


detector = ZeroDetector()


detector.SGD(
      training_pairs,
      eopchs = 10,
      learning_rate = 0.01

)

score = 0
elts_to_check = 1000




for i in range(elts_to_check):
      x = training_data[0][i]
      label = training_data[1][i]
      p = detector.predict(x)
      
      if(label == 0):
            print("WE'VE GOT A ZERO!")
            if(p>0.9):
                  print("SUCCESS!")
      