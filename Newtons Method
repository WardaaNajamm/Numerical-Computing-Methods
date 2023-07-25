from sympy import symbols
import math
import sympy as sp
def newtonsmethod(func,funcderiv,x,n):
  def f(x):
   f=eval(func)
   return f
  def df(x):
   df=eval(funcderiv)
   return df
  for intercept in range (1,n):
   i =x-(f(x)/df(x))
   x=i
   

  print("The root was found to be at ",x,"after ",n," iterations")

x,y =symbols('x y')
func=input("Enter Function: ")
expr=func
expr=eval(func)

funcd=str(sp.diff(func))
expr1=funcd
expr1=eval(funcd)
print("The derivate of function is : ",funcd)
x=int(input("Enter initial point: "))
n=int(input("Enter number of iterations: "))
newtonsmethod(func,funcd,x,n)


#x**3 + 3*x**2 +2
