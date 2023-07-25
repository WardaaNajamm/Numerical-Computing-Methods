import math
from sympy import symbols
import numpy


def f(x):
      f =  eval(func)
      return f

def regula_falsi(func,a,b,error):
    i = 1
    print('\n\nIterations:')
    flag = 1
    while flag:
        c = a - (b-a) * f(a)/( f(b) - f(a) )

        if f(a)*f(b) > 0.0:
            print('No root lies between entered values. Try again.')

        print("I= ",i," c= ",c,"f(c)= ",f(c))
        if f(a)*f(c) <0.0 :
            b = c
            i = i + 1
        else:
            i = i + 1
            a = c

        
        flag = abs(f(c)) > error

    print('\nRoot: %0.8f' % c)

x,y =symbols('x y')
func=input("Enter Function: ")
expr=func
#expr1=eval(func)

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
error = float(input('Enter value of tolerable error: '))
regula_falsi(expr,a,b,error)
