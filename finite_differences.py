# Week 3 Assignment 4
# Write a finite difference calculation of the Lennard-Jones force, such that the error with respect to the analytic result is smaller than 1.e-8
#
# Authors: Oliviero Andreussi, Student
# 
# Variables: 
#   epsilon, sigma: parameters of the Lennard-Jones potential, in a.u.
#   h: finite-difference parameter
#   flj_analytic: analytic result of the Lennard-Jones force, in a.u.
#   flj_numerical: numerical result of the Lennard-Jones force, in a.u.
#
import numpy as np
epsilon=4.e-4 # in a.u.
sigma=6 # in a.u.

r= #this can be an hardcoded value or taken in input from the user

h= #as you need to figure out the value, it would be a good idea to do a loop over increasingly small values

flj_analytic= # this should be the exact analytic result for the force

flj_numerical= # this is the expression that uses the values of the LJ potential at r and r+h

print() # print the value of x, the value of h, and the associated error
