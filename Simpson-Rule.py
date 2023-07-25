#Simpson 1/3rule

#function to integrate
def f(x):
  return 1/(1+x**2)

#Implementing Simpson's 1/3
def simpson(x0,xn,n):
  h=(xn-x0)/n            #calculating step size h
  
  integration=f(x0) + f(xn)        #find sum

  for i in range(1,n):
    k = x0 + i*h
    if i%2 == 0:
        integration = integration +2 * f(k)  #even terms
    else:
        integration = integration +4 * f(k)  #odd terms

#calculate value
  integration = integration * h /3

  return integration

#Input 
lower_limit = float (input("Enter lower limit of integration: "))
upper_limit = float (input("Enter upper limit of integration: "))
sub_interval = int (input("Enter sub interval of integration: "))

#call trapezoidal() and get result 
result=simpson(lower_limit,upper_limit,sub_interval)
print("Integration result by Simpson 1/3 method is %0.6f " % (result))
