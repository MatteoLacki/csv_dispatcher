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
    cmd, cmdpdf = dia_nn(**args)
    run(cmd)
    run(cmdpdf)

def maxquant_foo(**args):
    gen_mqpar(**args)
    cmd= rf"powershell.exe dotnet {args['exe_path']} {args['output_path']}/{args['exp_name']}.xml"
    run(cmd)

def print_foo(x,y,z):
    return print(foo(x,y,z))

def foo2(number, string):
    print(number + number)
    print(string)