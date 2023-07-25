import sympy as sy
from sympy import *
import numpy as np
import math
import parser
from numpy import *
import pandas as pd
x1 = symbols('x')
x2 = symbols('x') 
x3 = symbols('x') 

print ("TRAPEZOIDAL METHOD: ")
def trapezoid(f1,a1,b1,n1):
  h1=float((b1-a1)/(n1))
  result1=0
  for i in range(1, n1): 
    x1 = a1 + i*h1 
    result1 = result1 + 2*eval(f1)

  result1 = result1 * h1/2 
  error1 = 2 - result1 
  print("Error is: ", error1)
  return result1

from math import exp, sin, cos, tan, exp, log
expression1 = input("Enter equation:")
a1 = input('Enter value of a: ') 
b1 = input('Enter value of b: ')

a1 = eval(a1) 
b1 = eval(b1) 

n1=int(input('Enter value n: '))

trapezoid_numerical=trapezoid(expression1, a1, b1, n1)

print('The numerical trapezoid value: ', trapezoid_numerical)

print("SIMPSON 1/3 METHOD:")
def simpson1(f2,a2,b2,n2):
  h2=float((b2-a2)/(n2))
  result2=0
  for i in range(1, n2): 
    x2 = a2 + i*h2 
    if i%2 == 0:
            result2 = result2 + 2 * eval(f2)
    else:
            result2 = result2 + 4 * eval(f2)

  result2 = result2 * h2/3 
  error2 = 2 - result2
  print("error is: ", error2)
  return result2

from math import exp, sin, cos, tan, exp, log
expression2 = input("Enter equation:")
a2 = input('Enter value of a: ') 
b2 = input('Enter value of b: ')

a2 = eval(a2) 
b2 = eval(b2) 

n2=int(input('Enter value n: '))

simpson1_numerical=simpson1(expression2, a2, b2, n2)

print('The numerical simpson value: ', simpson1_numerical)

print ("SIMPSON 3/8 METHOD: ")
def simpson38(f3,a3,b3,n3):
  h3=float((b3-a3)/(n3))
  result3=0
  for i in range(1, n3): 
    x = a3 + i*h3
    if i%2 == 0:
            result3 = result3 + 2 * eval(f3)
    else:
            result3 = result3 + 3 * eval(f3)
    result3 = result3 + 2*eval(f3)

  result3 = result3 * 3 * h3/8 
  error3 = 2 - result3
  return result3

from math import exp, sin, cos, tan, exp, log
expression3 = input("Enter equation:")
a3 = input('Enter value of a: ') 
b3 = input('Enter value of b: ')

a3 = eval(a3) 
b3 = eval(b3) 

n3=int(input('Enter value n: '))

simpson38_numerical=simpson38(expression3, a3, b3, n3)

print('The numerical simpson 3/8 value: ', simpson38_numerical)
