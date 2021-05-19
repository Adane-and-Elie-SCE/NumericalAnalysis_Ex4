#  Adane Adgo - 315721969
#  Elie Bracha -

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive():
    x = sp.symbols('x')
    pol = 4*x**4 + -8*x**3 + x**2 - 3*x + 9
    rng = (-2, 2)
    eps = 0.0001

    print("p(x) = ", pol, ",Range = ", rng, ", epsilon = ", eps)
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")

    if choice == '1':
        Bisection_Method(lambdify(x, pol), rng, eps)

    elif choice == '2':
        sol = Newton_Raphson(lambdify(x, pol), rng, eps)

    elif choice == '3':
        sol = secant_method(lambdify(x, pol), rng, eps)
    else:
        print("Invalid choice")

    print(sol)

def create_range(f):
    for i in range(-10, 10):



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
