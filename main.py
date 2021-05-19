#  Adane Adgo - 315721969
#  Elie Bracha -

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive(func, big_range, epsilon, step):

    print("f(x) = ", func, ",Range = ", big_range, ", epsilon = ", epsilon)
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")

    if choice == '1':
        method = Bisection_Method

    elif choice == '2':
        method = Newton_Raphson

    elif choice == '3':
        method = secant_method

    else:
        print("Invalid choice")
        return

    solver(func, big_range, epsilon, step)


def solver(unc, big_range, epsilon, step, method):
    left_bound, right_bound = big_range
    a = left_bound, b = left_bound + step

    while b<=



def Bisection_Method(pol, little_range, eps):
    return 1


def Newton_Raphson(pol, little_range, eps):
    return True


def secant_method(pol, little_range, eps):
    return True


x = sp.symbols('x')
user_func = 4*x**3 + -8*x**3 + x**2 - 3*x + 9
user_range = (-10, 10)
user_epsilon = 0.0001
user_step = 0.1


# Drive(user_func, user_big_range, user_epsilon, user_step)
