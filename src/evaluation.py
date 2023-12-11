import numpy as np
from src.forward_propagation import ForwardPropagation

forward_propagation = ForwardPropagation()

class Evaluation:
    """
    This class defines some functions to evaluate the trained model
    """

    def predictions(self, A):
        return np.argmax(A, 0)
    

    def accuracy(self, predictions, Y):
        return np.sum(predictions == Y) / Y.size
    
    
    def validation_predictions(self, X, weights, biases):
        forward_output = forward_propagation.forward_propagation(weights, biases, X)
        key, value = list(forward_output.items())[-1]
        prediction = self.predictions(value)
        return prediction