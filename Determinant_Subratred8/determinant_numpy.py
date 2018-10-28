# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:17:24 2018

@author: OM
"""
import numpy as np
import numpy.linalg as m
matrix1= np.matrix([[8,2,7],[4,6,9],[1,5,3]])
matrix1
print (matrix1)

m.det(matrix1)
print (m.det(matrix1))

round(m.det(matrix1))
print (round(m.det(matrix1)))

int(round(m.det(matrix1)))
print (int(round(m.det(matrix1))))