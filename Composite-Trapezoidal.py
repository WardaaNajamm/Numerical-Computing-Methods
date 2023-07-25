import numpy as np
import math
import numpy as geek

#INPUT FROM USER
#a = float (input("Enter lower limit of integration: "))
#b = float (input("Enter upper limit of integration: "))
#n = int (input("Enter value of n: "))
#we can also take input of function from user
#equation=input("Enter equation:")

#hardcoded values
a = 1
b = 2
n = 4
h = (b - a) / n
x = np.linspace(a, b, n+1)
print(x)

f = x * (np.log(x))
sum=0
for i in range(1,n):
  sum = sum + f[i]
I_trap = (h/2)*(f[0] + 2 * sum + f[n])

print(I_trap)
