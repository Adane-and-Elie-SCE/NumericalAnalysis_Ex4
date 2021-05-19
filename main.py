#  Adane Adgo - 315721969
#  Elie Bracha -

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive():
    x = sp.symbols('x')
    func = 4*x**3 + -8*x**3 + x**2 - 3*x + 9
    big_range = (-10, 10)
    eps = 0.0001
    print("f(x) = ", func, ",Range = ", big_range, ", epsilon = ", eps)
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")

    if choice == '1':
        method = Bisection_Method

    elif choice == '2':
        method = Newton_Raphson

    elif choice == '3':
        method = secant_method
    else:
        print("Invalid choice")

    print(sol)


def solver():



def Bisection_Method(f, rng, eps):
    a, b = rng
    while abs(b - a) > eps:
        c = (a + b)/2
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

    x = (a + b)/2


def Newton_Raphson(pol, rng, eps):
    return True


def secant_method(pol, rng, eps):
    return True


Drive()
