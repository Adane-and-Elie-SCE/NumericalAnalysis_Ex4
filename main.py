#  Adane Adgo - 315721969
#  Elie Bracha -

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive():
    x = sp.symbols('x')
    func = 4*x**4 + -8*x**3 + x**2 - 3*x + 9
    big_range = (-10, 10)
    little_range = create_range(big_range, lambdify(x, func))
    eps = 0.0001

    print("p(x) = ", func, ",Range = ", little_range, ", epsilon = ", eps)
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")

    if choice == '1':
        Bisection_Method(lambdify(x, func), little_range, eps)

    elif choice == '2':
        sol = Newton_Raphson(lambdify(x, func), little_range, eps)

    elif choice == '3':
        sol = secant_method(lambdify(x, func), little_range, eps)
    else:
        print("Invalid choice")
    print(sol)


def create_range(big_range, f):
    left_bound, right_bound = big_range
    a, b = left_bound, left_bound + 1
    while f(a) * f(b) >= 0 and b <= right_bound:
        a += 0.1
        b += 0.1
    return [a, b]


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
