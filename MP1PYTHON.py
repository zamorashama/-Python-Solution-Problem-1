import matplotlib.pyplot as plt
import numpy as np
def f(n):
    if n <= 9:
        return n*n-7
    return f(n-10)

if __name__ == '__main__' :
    x = []
    y = []
    for i in range(1,100):
        x.append(i)
        y.append(f(i))
        
        print(x)
        print(y)
        plt.stem(x,y)
        
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        
        plt.title( 'The graph for f(n)' )
       
        plt.show()