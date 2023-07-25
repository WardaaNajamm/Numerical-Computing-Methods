import numpy as np

#taking input for the number of x values which will eventually be the same for y values
no = int(input('Enter number of data points: '))
x = np.zeros((no))
y = np.zeros((no,no))

#taking input for x and y 
print('Enter data for x and y: ')
for i in range(no):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
for i in range(1,no):
    for j in range(no-1,i-2,-1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

#generating the backward difference table         
print('\nBACKWARD DIFFERENCE TABLE\n');
for i in range(0,no):
    print('%0.2f' %(x[i]), end='')
    for j in range(0,i+1):
        print('\t\t%0.7f' %(y[i][j]), end='')
    print()

#calculating the value of p for f(x)     
print('\nFinding f(x) at x\n');
def p_cal(p, no):
    temp = p;
    for i in range(1, no):
        temp = temp * (p + i);       
    return temp;

#calculating factorial for denominator for f(x)    
def fact(no):
    f = 1;
    for i in range(2, no + 1):
        f *= i;
    return f;

#taking input for the value of x     
x_val = float(input('Enter value of x at which you want to find f(x): '))

#solving for f(x) at the value of x 
fx = y[no-1][0];  
p = (x_val - x[no-1]) / (x[1] - x[0]);     
for i in range(1,no):
    fx = fx + (p_cal(p, i) * y[no-1][i]) / fact(i);  
 
print("\nValue at", x_val,
      "is", round(fx, 7));
