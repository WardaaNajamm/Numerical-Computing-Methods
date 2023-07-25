import sympy as sy
from sympy import *
import numpy as np
import math
import parser
from numpy import *
import pandas as pd
x = symbols('x') # We need this so we can plug different values of x into the expression with eval()

def midpoint(f,a,b,n):
  h=float((b-a)/(n+2))
  result=0
  for i in range(0, n+1, 2): #Loop goes from 0 to n+1, with increments of 2 (because we only take even values)
    x = a + (i+1)*h # This is the value of x that will be plugged into the expression with eval
    result = result + eval(f)

  result = result * 2*h # Multiply final sum with 2h (because formula)
  return result

from math import exp, sin, cos, tan, exp, log
expression = input("Enter equation:")
a = input('Enter value of a: ') # User can type 'pi/4' etc to enter pi intervals
b = input('Enter value of b: ')

a = eval(a) # To evaluate pi and convert it to a number
b = eval(b) 

n=int(input('Enter value n: '))

midpoint_numerical=midpoint(expression, a, b, n)

print('The numerical midpoint value: ', midpoint_numerical)

