import math
import numpy

def bisection_method(func, a, b, user_error):
  def f(x):
    f = eval(func)
    return f
  i=0
  error= abs(b-a)

  while error > user_error:
    c=(a+b)/2

    if f(a) * f(b) >=0:
      print("No solution")
      break

    elif f(c) * f(a) < 0:
      b=c
      error= abs(b-a)
      i=i+1
    
    elif f(c) * f(b) < 0:
      a=c
      error= abs(b-a)
      i=i+1
    
    else:
      print("Error")

    print("The error is:", error)
    print("The lower bound is:", a)
    print("The upper bound is:", b)
    print("Number of iterations are:", i)
  

equation=input("Enter equation:")
lb=int(input("Enter lower bound value:"))
ub=int(input("Enter upper bound value:"))
e=float(input("Enter acceptable error:"))
bisection_method(equation, lb, ub, e)

#math.cos(x) + 3*x - 3
#x**3 + 4*x**2 - 10
#1
#2
#0.0001
