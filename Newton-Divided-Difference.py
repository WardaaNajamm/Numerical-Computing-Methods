import numpy as np

def newton_divided_difference(x, y):
    """
    x: an array containing x values.
    y: an array containing y values.
    Returns:
        f: an array containing Newton's divided difference coefficients.
    """
    n = x.size
    q = np.zeros((n, n))

    # Insert 'y' in the first column of the matrix 'q'
    q = np.concatenate((y[:, None], q), axis=1)

    for j in range(1, n):
        for i in range(j, n):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

    # Copy the diagonal values of the matrix q to the vector f
    f = np.zeros(n)
    for i in range(0, n):
        f[i] = q[i, i]

    print('\nDIVIDED DIFFERENCE TABLE\n');

    for i in range(0,n):
       print('%0.2f' %(x[i]), end='')
       for j in range(0, n):
          print('\t\t%0.8f' %(q[i,j]), end='')
       print()

    # Prints the polynomial
    print("\n\nThe polynomial is:")
    print("p(x)={:+.8f}".format(f[0]), end="")
    for i in range(1, n):
        print("{:+.8f}".format(f[i]), end="")
        for j in range(1, i + 1):
            print("(x{:+.2f})".format(x[j-1] * -1), end="")
    print("")

    print('\nFinding f(x) at x 1\n');
    
    def cal(l, no):
        temp=1;
        for i in range(0, no):
            temp = temp * (l - x[i]);     
        return temp;

    x_val = float(input('Enter value of x at which you want to find f(x): '))
    fx = q[0][0];
    #u = (x_val - x[n-1]);     
    for i in range(1,n):
        fx = fx + (cal(x_val,i) * q[i][i]);  
    
    print("\nValue at", x_val,
          "is", '%0.8f' %fx);

    return [f]

"""
a1 = np.array(['1.0', '1.3', '1.6', '1.9', '2.2'])
a = a.astype(float)
b1=np.array(['0.7651977', '0.6200860', '0.4554022', '0.2818186', '0.1103623'])
b = b.astype(float)

"""

# Reading number of unknowns
p = int(input('Enter number of data points: '))

# Making numpy array of p & p x n size and initializing 
# to zero for storing x and y value along with differences of y
a = np.zeros((p))
b = np.zeros((p))

# Reading data points
print('Enter data for x and y: ')
for i in range(p):
    a[i] = float(input( 'x['+str(i)+']='))
    b[i] = float(input( 'y['+str(i)+']='))


newton_divided_difference(a,b)

