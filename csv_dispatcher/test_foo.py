import numpy as np
from limspy.dia_nn import dia_nn

def foo(dicto):
	#Experiment,Fasta,Outdir,Spectrallib,Exe,FDR,Cut,Missedcl,Pepmin,Pepmax,Precmin,Precmax,Fragmin,Fragmax,Massaccuracy,MS1accuracy,massaccuracycal,ProteinGroup,Quantification,Normalisation,Librarygen,NN,mbr,individualruns,Threads
    #dia_nn(experiments=Experiment,fastas=Fasta,threads=Threads,fdr=FDR,min_pep_len=Pepmin,max_pep_len=Pepmax,max_fr_mz=Fragmax,min_fr_mz=Fragmin, min_pr_mz=Precmin,max_pr_mz=Precmax, normalisation=Normalisation,miss_cleavages=Missedcl,cut=Cut,quantification=Quantification, exe_path=Exe)
    cmd= dia_nn(**dicto)
    return cmd

def print_foo(x,y,z):
    return print(foo(x,y,z))

def foo2(number, string):
    print(number + number)
    print(string)add