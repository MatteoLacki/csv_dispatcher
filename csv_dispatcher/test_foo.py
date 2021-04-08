import numpy as np
from subprocess import run
from limspy.dia_nn import dia_nn

def foo(x,y,z):
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    return x,y,z

def diann_foo(**args):
	cmd, cmdpdf = dia_nn(**args)
	run(cmd)
	run(cmdpdf)

def print_foo(x,y,z):
    return print(foo(x,y,z))

def foo2(number, string):
    print(number + number)
    print(string)