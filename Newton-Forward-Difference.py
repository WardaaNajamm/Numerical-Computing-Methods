import numpy as np
#taking input for the number of x values which will eventually be the same for y values
n = int(input('Enter number of data points: '))
x = np.zeros((n))
y = np.zeros((n,n))

#taking input for x and y 
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

#generating the forward difference table  
print('\nFORWARD DIFFERENCE TABLE\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.7f' %(y[i][j]), end='')
    print()
    
#calculating the value of p for f(x)  
print('Finding polynomial at the value given\n');
def p_cal(p, n):
    temp = p;
    for i in range(1, n):
        temp = temp * (p - i);       # u + i
    return temp;
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;
value1 = float(input('Enter the value: '))
sum = y[0][0];  #y[n][n]
p = (value1 - x[0]) / (x[1] - x[0]);     # - x[n]
for i in range(1,n):
    sum = sum + (p_cal(p, i) * y[0][i]) / fact(i);  #y[n][i]
 
print("\nValue at", value1,
      "is", round(sum, 6));

"""
Enter number of data points: 2
Enter data for x and y: 
x[0]=2
y[0]=2.22
x[1]=3
y[1]=3.33
2.5
"""
