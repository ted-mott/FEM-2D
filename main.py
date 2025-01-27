"""
FEM-2D

Python script to run sequential FEM solver and Topology optimisation of a set square grid problem
Understand generation of grid .etc.
Aim to create a seperate FEA solver in a different doc
Aim to display each iteration/ save iterations 1,10 and 100 for comparison and display stress values?


09-01-25
Ted M

"""
#importing packages
import numpy as np
import matplotlib
import scipy

"___defining variables_________________________"
#number of iterations
noOfIterations = 100
#grid size
numRows, numColumns = 100,100


"___Boundary conditions________________________"
#fixed at...

#force at...



def main():
    for i in range (0,noOfIterations):
        print(i)

def FEMsolver():
    pass

if __name__ == "__main__":
    main()
    