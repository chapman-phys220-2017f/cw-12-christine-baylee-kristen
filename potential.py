#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Baylee Mumma, Christine Outlaw
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 12

import numpy as np
import matplotlib.pyplot as plt

def plot():
    """plot():
    Generates the sombrero potential plot."""
    t = np.linspace(-1.5,1.5,100)
    V = t**4/4-t**2/2
    plt.plot(t,V)
    plt.xlabel("position")
    plt.ylabel("potential")
    plt.title("Sombrero potential curve")
    plt.show()