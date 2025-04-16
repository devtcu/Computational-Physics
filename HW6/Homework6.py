import numpy as np
from localpackages.calculus.ODE import fourth_runge_kutta


def f(x,t):
    return -x**3 + np.sin(t)
def f2(x,t):
    return -x**3 + np.cos(t)
def f3(x,t):
    return -x**3 + np.tan(t)

def main():
    
    ans = fourth_runge_kutta(f)
    ans2 = fourth_runge_kutta(f2)
    ans3 = fourth_runge_kutta(f3)
    return ans, ans2, ans3
    
if __name__ == "__main__":
    main()
