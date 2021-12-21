import numpy as np
import  math

class activation_funcs:
    def __init__(self):
        self.e=math.e
    def sigmoid(self,x):
        x= 1/(1+ self.e-x)
        return x
    def relu(self,x):
        if x<=0:
            x=0
            return x
        else:
            return x
    def tanh(self,x):
        x = (2/(1 + np.exp(-2*x))) -1
        return x
    def softmax(self,x):
        x = np.exp(x)
        x = x/x.sum()
        return x
    def Leaky_Relu(x,a=0.01):
        if x>0:
            return x 
        else: 
            x=a*x
            return x
    def elu(x, a):
        if x<0:
            x= a*(np.exp(x)-1)
            return x
        else:
            return x  
        
