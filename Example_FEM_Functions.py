import numpy as np

def assignBoundraryConditions(NodeList, ExtendedNodeList):
    ProblemDimension = np.size(NodeList, 1)
    NumberOfNodes = np.size(NodeList, 0)

    DegreesOfFreedom = 0
    DegreesOfC = 0

    for i in range(0,NodeList):
        for j in range(0,ProblemDimension):
            