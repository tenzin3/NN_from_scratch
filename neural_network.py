import math
import numpy as np
from typing import List 
from neuron import Neuron


class NeuralNetwork:
    def __init__(self, shape: List[int]):
        self.shape = shape
        self.layers = self.generate_layers()

    def generate_layers(self):
        layers = {}
        for idx, num_neurons in enumerate(self.shape):
            layers[idx] = []
            if idx == 0:
                for _ in range(num_neurons):
                    curr_neuron = Neuron(np.random.randn())
                    layers[idx].append(curr_neuron)
            else:
                for _ in range(num_neurons):
                    prev_neurons = layers[idx - 1]
                    curr_neuron = prev_neurons[0].tanh()
                    for neuron in prev_neurons[1:]:
                        curr_neuron.__add__(neuron.tanh())
                    layers[idx].append(curr_neuron)
        return layers


# Example usage:
NN = NeuralNetwork([2, 3, 1])
for idx, layer in NN.layers.items():
    print(f"Layer {idx}: {[neuron for neuron in layer]}")