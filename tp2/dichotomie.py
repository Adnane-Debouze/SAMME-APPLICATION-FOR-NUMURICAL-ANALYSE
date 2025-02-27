import math

import numpy


def f1(x):
    return pow(x,3)+2*x-7
def f2(x):
   return 2*numpy.sin(x)-x
def dicho(a,b,e):
    while(b-a>e):
        m=(a+b)/2
        if f1(a)*f1(m)<0:
            b=m
        else:
            a=m
    return (a+b)/2
print('f1 : ',dicho(1.5,2.5,0.5 *pow(10,-2)))
def dicho2(a,b,e):
    while(b-a>e):
        m=(a+b)/2
        if f2(a)*f2(m)<0:
            b=m
        else:
            a=m
    return (a+b)/2
print('f2 : ',dicho2(1,2,pow(10,-3)))
print('f2 ( dicho) : ',f2(dicho2(0,2,pow(10,-3))))