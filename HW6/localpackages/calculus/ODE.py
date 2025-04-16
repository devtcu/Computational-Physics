def trapezoid(func, a, b, n):
    h = float(b - a) / n   
    summation = 0

    
    for k in range(1, n):
        summation += func(a + k * h)
    
    return h * (0.5 * func(a) + 0.5 * func(b) + summation)
            
def summ(a,b):
    return a + b          


# code
import numpy as np
import matplotlib.pyplot as plt 

def fourth_runge_kutta(f):
    
    final_x = []

    #initial conditions
    first = 0
    last = 10
    h = (last - first) / 100 #step size
    x = 0

    t = np.arange(0, 10, h)

    for final_t in t:
        final_x.append(x)
        k_1 = h * f(x, final_t)
        k_2 = h * f(x + (1 / 2) * k_1, final_t + (1 / 2) * h)
        k_3 = h * f(x + (1 / 2) * k_2, final_t + (1 / 2) * h)
        k_4 = h * f(x + k_3, final_t + h)
        x += (1 / 6) * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
        

    plt.plot(t, final_x)
    plt.show()


