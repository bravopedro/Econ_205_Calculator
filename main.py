import sympy as sp
from sympy import Derivative, solve, symbols, Eq
from sympy.solvers import solve

print("1 Derivative")
print("2 First Order Condition")
print("3 Marginal Product of Capital")
print("4 Marginal Product of Labor")
print("5 Calculate the IsoQuant")
print("6 Constant decreasing increasing returns to scale")
print("7 Solve for L or K")
print("8 Find the production function")
print("9 Marginal Rate Of Technical Substitution")
print("10 Solve for the supply curve ")
print("12 Cost Function")
print("13 Long run equilibrium number of firms")
print("14 Find the competitive equilibrium price")
print("15 Price after Tax")
print("16 Dead Weight Loss")
print("17 Producer Surplus")
print("18 Consumer Surplus")
print("19 Total Welfare")
print("20 Pareto effect or no")
print("21 Marginal utility of a ")
print("22 Marginal utility of b ")
print("23 Optimal Choice")


print("REMINDER Always Remember to type ot ex.) 3x^2 = 3*x**2 (Use decimals not fractions)")
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

if choice == 10:
    # supply curve
    q = sp.Symbol('q')
    f1 = input("Enter Your Expression (lowercase q and p):  ")
    print("q = ")
    print(f1.diff(q))

if choice == 11:
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

if choice == 12:
    # find max vc available to spend  and still be profit maximizing
    r =input("What is R")
    f = input("What is F")
    print(r ,' is the maximum cost because you cant spend more than you earn')

if choice == 13:
    #3 given a cost function give the long run equilibrium number of firms
    q = symbols('q') # everytime q is mentioned in the input it will be viewed as a symbol
    costFunction = input("Enter the Cost Function")
    numFirms = input("Enter the number of firms available")
    deriv = costFunction.diff('q') # takes the derivative of the cost function
    deriv = str(deriv) #
    divByQ = costFunction / q # divides the cost function by q
    divByQ = str(divByQ)
    total = deriv + " = " + divByQ # this is where I get stcuk I cannot set them equal to
                                    # each other and solve for q
    print(total)















