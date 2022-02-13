import math
import numpy as np
from activation_funcs import sigmoid



class feed_forward():
  def __init__(self):
    np.random.seed(12)
    self.w1 = np.random.randn()
    self.w2 = np.random.randn()
    self.w3 = np.random.randn()
    self.w4 = np.random.randn()
    self.w5 = np.random.randn()
    self.w6 = np.random.randn()
    self.bias = 0
    self.sigmoid = sigmoid


  def forward(self, inputs):
     self.x1, self.x2 = inputs
     self.a1 = self.w1*self.x1 + self.w2*self.x2 + self.bias
     self.h1 = self.sigmoid(self.a1)
     self.a2 = self.w3*self.x1 + self.w4*self.x2 + self.bias
     self.h2 = self.sigmoid(self.a2)
     self.a3 = self.w5*self.h1 + self.w6*self.h2 + self.bias
     self.h3 = self.sigmoid(self.a3)
     return self.h3

