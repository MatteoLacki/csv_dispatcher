import numpy as np
from subprocess import run
from limspy.dia_nn import dia_nn
from limspy.parse_mqpar import gen_mqpar

def foo(x,y,z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    return x,y,z

def diann_foo(**args):
    dia_nn(**args)

def maxquant_foo(**args):
    gen_mqpar(**args)

def print_foo(x,y,z):
    return print(foo(x,y,z))

def foo2(number, string):
    print(number + number)
    print(string)