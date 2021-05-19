#  Adane Adgo - 315721969
#  Elie Bracha -
import math

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive(pol, big_range, epsilon, step):

    print("f(x) = ", pol, ",Range = ", big_range, ", epsilon = ", epsilon)
    Solver(pol, big_range, epsilon, step, method_picker())


def method_picker():
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")

    if choice == '1':
        print("Bisection Method")
        return Bisection_Method

    elif choice == '2':
        print("Newton_Raphson")
        return Newton_Raphson

    elif choice == '3':
        print("secant_method")
        return secant_method


def Solver(pol, big_range, epsilon, step, method):

    left_bound, right_bound = big_range
    f = lambdify(x, pol)
    df = lambdify(x, sp.diff(pol))

    #  function
    a, b = left_bound, left_bound + step
    while b <= right_bound:

        if f(a) * f(b) < 0:
            solution = method(f, (a, b), epsilon)
            sol, iterations = solution
            if solution is not None:
                print("x = " + str(sol) + ", number of iteration: " + str(iterations))
        a += step
        b += step

    #  derivative
    a, b = left_bound, left_bound + step
    while b <= right_bound:

        if df(a) * df(b) < 0:
            solution = method(f, (a, b), epsilon)
            sol, iterations = solution
            if solution is not None and abs(f(sol)) < epsilon:
                print("x = " + str(sol) + ", number of iterations : " + str(iterations))
        a += step
        b += step


def Bisection_Method(f, little_range, epsilon):
    a, b = little_range
    k = math.ceil(- math.log(epsilon/(b - a), math.e) / math.log(2, math.e))
    counter = 0

    while abs(b - a) > epsilon:
        c = (a + b) / 2

        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

        counter += 1

    c = (a + b) / 2
    if counter <= k:
        return c, counter


def Newton_Raphson(pol, little_range, eps):
    return True


def secant_method(pol, little_range, eps):
    return True

1
x = sp.symbols('x')
user_func = x**4 + x**3 + -3*x**2
user_range = (-10, 10)
user_epsilon = 0.0001
user_step = 0.1


Drive(user_func, user_range, user_epsilon, user_step)
