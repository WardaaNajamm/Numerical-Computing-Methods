#lagrange interpolation
import numpy as np
import math
import matplotlib.pyplot as plt
import numpy as np

n = int(input('Enter number of data points: '))
print('Degree of Polynomial : %.1f ' %(n-1))
#array of n
x = np.zeros(n)
y = np.zeros(n)


equation=input("Enter equation:")
def f(x):
    f = eval(equation)
    return f

print('Enter data for x ')             #print x and y
for i in range(n):
  x[i] = float(input('x['+str(i)+']='))
  y[i]=f(x[i])

xp=float(input('Enter interpolation point '))
yp=0

#implementation of lagrange formula
for i in range(n):

  p=1

  for j in range(n):
    if i!=j: 
      p = p*(xp-x[j]) / (x[i]-x[j])


  yp = yp + p * y[i]
#math.cos(x) + 3*x - 3
#Output
print('Interpolated value : %.3f is %.7f. ' % (xp,yp))

plt.plot(x,y,'ro', x , y ,'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
