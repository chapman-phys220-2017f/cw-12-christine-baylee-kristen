#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Baylee Mumma, Christine Outlaw
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 12

import numpy as np
import nose
import sombrero as sm

"""Sombrero test functions"""

def test_1():
    desired = 1
    t,x,y = sm.rk4(0, 5, 1, 0, 0, 0)
    actual = x[4]
    nose.tools.assert_almost_equal(desired,actual,4)

def test_2():
    desired = 0
    t,x,y = sm.rk4(0, 5, 0, 0, 0, 0)
    actual = x[4]
    nose.tools.assert_almost_equal(desired,actual,4)
