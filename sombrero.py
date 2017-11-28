#!/usr/bin/env python3
# Name: Baylee Mumma, Christine Outlaw, Kristen Peet
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 12

import numpy as np
import matplotlib.pyplot as plt

def x_dot(y):
    """x_dot(y)
         Describes the differential equation for position as given in CW 12.
    """
    return y

def y_dot(t,y,x,nu,F):
    """y_dot(t,y,x,nu,F)
         Describes the differential equation for velocity as given in CW 12.
    """
    return -(nu*y)+x-(x**3)+(F*np.cos(t))


def rk(a, b, x0, y0, nu=0, F=0, xdot = x_dot, ydot = y_dot):
    """rk(a, b, x0, y0, nu=0, F=0, xdot = x_dot, ydot = y_dot)
          input:
             a - float, beginning point of the time domain, such that t_initial = 2pi*a
             b - float, end point of time domain, such that t_final = 2pi*b
             x0 - float, initial position of the ball
             y0 - float, initial velocity of the ball
             nu - float, constant damping parameter
             F - float, constant force amplitude parameter
             xdot - function, part of the coupled differentiial equation.  The correct function
             for xdot is passed in to rk.
             ydot - function, part of the coupled differentiial equation.  The correct function
             for ydot is passed in to rk.
          output: (t,x_vec,y_vec)
             t - numpy array, with mesh spacing dt = 0.001
             x_vec - numpy array, contains the position of the ball at each time in the linspace
             y_vec - numpy array, contains the velocity of the ball at each time in the linspace
       All output numpy arrays are the same length, as determined by the input parameters 'a' and 'b'.
             """
    
    
    
    
    
    
    
    
    
    
    
    
    