"""
Following tutorial:
https://www.youtube.com/watch?v=tv1TlAebvm0&list=PLnT2pATp7adWUaMh0A8jfoN_OHGAmt_m4&index=2

Nodes and Elements

NoN Number of Nodes
NPE Nodes per element
ENL Extended node list
NoE number of elements
PD problem dimension

"""

import numpy as np
from Example_FEM_Functions import *

NodeList = np.array([[0,0], 
                     [1,0], 
                     [0.5,1]])

#coordinates
ElementList = np.array([[1,2], 
                        [2,3], 
                        [3,1]])

#order of elements doesn't matter

BoundaryConditions = np.array([[-1, -1], 
                               [1, -1], 
                               [1, 1]])

#1 for free to move, -1 for fixed

Forces = np.array([[0 , 0], 
                   [0, 0], 
                   [0, -20]])

Displacements = np.array([[0, 0], 
                          [0, 0], 
                          [0,0]])

YoungsModulus = 10**6
CrossSectionalArea = 0.01

ProblemDimension = np.size(NodeList, 1)

#size for each element

NumberOfNodes = np.size(NodeList, 0)

ExtendedNodeList = np.zeros([NumberOfNodes, 6*ProblemDimension])

ExtendedNodeList[:,0:ProblemDimension] = NodeList[:,:]
#Assigning known node list

ExtendedNodeList[:,ProblemDimension:2*ProblemDimension] = BoundaryConditions[:,:]

(ExtendedNodeList, DegreesOfFreedom, DegreesOfCs ) = assignBoundraryConditions(NodeList, ExtendedNodeList)