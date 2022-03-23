import math
import sympy as sp
from mpmath import sqrt
from scipy.misc import derivative
from sympy import Derivative, solve, symbols



print("1 Derivative")
print("2 First Order Condition")
print("3 MPK")
print("4 MPL")
print("5  L* k*")
print("6 IsoQuant")
print("7 MRTS")
print("12 Cost Function")
print("9 Find L* or K* ")
print("Always Remember to type ot ex.) 3x^2 = 3*x**2 (Use decimals not fractions)")
choice = input("ENTER CHOICE NUM ")

if choice == 1:
    x = sp.Symbol('x')
    function = input("Enter Your Expression:  ")
    print(function.diff(x))
if choice == 2:
    var = sp.Symbol('x')            # the issue stems from the definition of x
    function = input("Enter Your Expression:  ")
    difFunction = function.diff(var) + " = 0"
    solve(difFunction, var)
if choice == 3:
    # MPK
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    f1 = input("Enter Your Expression (capital K and L):  ")
    print("because this is a MPL partial char will be L")
    partialChar = 'K'
    partialDeriv = Derivative(f1, partialChar)
    print(partialDeriv.doit())

if choice == 4:
    #MPL
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    f1 = input("Enter Your Expression (capital K and L):  ")
    print("because this is a MPL partial char will be L")
    partialChar = 'L'
    partialDeriv = Derivative(f1, partialChar)
    print( partialDeriv.doit())

if choice == 5:
    # calculate the isoquant given units of output
    exp = input("Enter Your Expression (capital K and L):  ")
    q = input("Enter q")
    print(q + " = " + exp)
if choice == 6:
    # CRS DRS IRS
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    kExp = input("What is K's Exponent: ")
    lExp = input("What is L's Exponent: ")
    if (kExp + lExp < 1):
        print("Function has Decreasing returns to scale")
    if (kExp + lExp == 1):
        print("Function has constant returns to scale")
    if (kExp + lExp  > 1):
        print("Function has increasing returns to scale")

if choice == 7:
    # solve for L or K
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    function = input("Enter Your Expression (capital K and L):  ")
    K = input("What is K* if unknown plug in 0")
    L = input("What is L* if unknown plug in 0")
    r = input("Enter r")
    w = input("Enter w")
    solveFor = (r*K + w*L)

    if(K == 0):
        theOne = symbols('K')
        K = solve((r * theOne + w * L), theOne)
        print("L:")
        print(L)
    if(L == 0):
        theOne = symbols('L')
        L = solve((r * K + w * theOne), theOne)
        print("L:")
        print(L)



if choice == 8:
    # production function
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    f1 = input("Enter Your ]Expression (capital K and L):  ")
    # remember we are solving for c(q)
    K = input("What is K* if unknown plug in zero")
    L = input("What is L* if unknown plug in zero")
    r = input("Enter r")
    w = input("Enter w")

if choice == 9:
    #MRTS
    K = sp.Symbol('K')
    L = sp.Symbol('L')
    f1 = input("Enter Your Expression (capital K and L):  ")
    partialChar = 'L'
    partialDeriv = Derivative(f1, partialChar)

    partialChar = 'K'
    partialDeriv2 = Derivative(f1, partialChar)
    print(partialDeriv2.doit() / partialDeriv.doit())

if choice == 12:
    # cost function
    print("fuck")
    # r = 2, w = 6, and  K = 4  2K 1/2 L 1/4
    # c(q) = lw + kr
    # (F(4, L) = 4L 1/4 = q
    # q = 4L^1/4 div by 4
    # q/4 = l^1/4 to the fourth
    # (q/4)^4 = l

    # f4 = input("Enter Your Expression (capital K and L):  ")

    # given = input("Whichever * is given ")
if choice == 13:
    # supply curve
    q = sp.Symbol('q')
    f1 = input("Enter Your Expression (lowercase q and p):  ")
    print("q = ")
    print(f1.diff(q))

if choice == 14:
    # long run equilibrium
    print("this one is hard")

if choice == 15:
    load = []
    #competetive market equilibrium price
    q = sp.Symbol('q')
    costFunc = input("Enter cost function")
    k = 0
    while(costFunc.length > k):
       if(costFunc[k] == 'q'):
           costFunc.remove(k)
           k = k + 1
    print(costFunc)

































