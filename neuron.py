import math 

class Neuron:
    def __init__(self, data:int,  _children=(), _op='', label='') :
        self.data = data
        self.grad = 0
        self._prev = set(_children)
        self._op = _op
        self.label = label


    def __repr__(self,) -> str:
        return f"Neuron(data={self.data})"

    def __add__(self, other):
        return Neuron(self.data + other.data,   (self, other), "+")

    def __mul__(self, other):
        return Neuron(self.data * other.data,   (self, other), "*")

    def __div__(self, other):
        return Neuron(self.data / other.data,   (self, other), "/")

    def __sub__(self, other):
        return Neuron(self.data - other.data,   (self, other), "-")
    
    def tanh(self):
        data = math.tanh(self.data)
        return Neuron(data, (self,), "tanh")


obj = Neuron(1, label="obj")
obj1 = Neuron(2, label="obj1")
obj2 = Neuron(-3, label="obj2")


obj3 = obj * obj1 + obj2
obj3.label = "obj3"
print(obj3)