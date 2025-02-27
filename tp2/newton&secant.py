import  math
import numpy as np
import math


def newton(a,b,e):
    c=a
    while abs(b-c)>e:
        c=b
        b=b-fx(b)/fxprim(b)
    return  b

def fx(x):
    return  math.exp(x)-2
def fxprim(x):
    return  math.exp(x)


def secante(a,b,e):
    c=b
    while np.abs(a-c)>e:
        c=a
        a=(a*fx(b)-b*fx(a))/ (fx(b)-fx(a))

        print(a)
    return a

def fx_n(x):
    return  np.exp(x)-2
print(secante(0,1,0.1))
print(newton(0,1,0.1))