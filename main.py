#  Adane Adgo - 315721969
#  Elie Bracha - 204795900

# https://github.com/Adane-and-Elie-SCE/NumericalAnalysis_Ex4.git

import math

import sympy as sp
from sympy.utilities.lambdify import lambdify


def Drive(pol, big_range, epsilon, step):

    print("f(x) = ", pol, ",Range = ", big_range, ", epsilon = ", epsilon)
    Solver(pol, big_range, epsilon, step, method_picker())


def method_picker():
    choice = input("[1] Bisection\n[2] Newton-Raphson\n[3] secant\nPick a Method:")
    print("\n")

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
    function_Solver(pol, big_range, epsilon, step, method)
    derivative_solver(pol, big_range, epsilon, step, method)


def function_Solver(pol, big_range, epsilon, step, method):
    f = lambdify(x, pol)
    left_bound, right_bound = big_range
    a, b = left_bound, left_bound + step

    while b <= right_bound:

        if f(a) * f(b) < 0:
            solution = method(pol, (a, b), epsilon)
            sol, iterations = solution
            if solution is not None:
                if abs(sol) < epsilon:
                    sol = 0
                print("x = " + str(sol) + ", number of iteration: " + str(iterations))
        a += step
        b += step


def derivative_solver(pol, big_range, epsilon, step, method):
    f = lambdify(x, pol)
    df = lambdify(x, sp.diff(pol, x))
    left_bound, right_bound = big_range
    a, b = left_bound, left_bound + step

    while b <= right_bound:

        if df(a) * df(b) < 0:

            if abs(df(b)) < epsilon or abs(df(a) < epsilon):
                solution = method(sp.diff(pol, x), (a - step, b + step), epsilon)
                sol, iterations = solution

            else:
                solution = method(sp.diff(pol, x), (a, b), epsilon)
                sol, iterations = solution

            if solution is not None and abs(f(sol)) < epsilon:
                if abs(sol) < epsilon:
                    sol = 0
                print("x = " + str(sol) + ", number of iterations : " + str(iterations))
                solution = None
        a += step
        b += step


def Bisection_Method(pol, little_range, epsilon):
    f = lambdify(x, pol)
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


def Newton_Raphson(pol, little_range, epsilon):
    f = lambdify(x, pol)
    df = lambdify(x, sp.diff(pol, x))
    x1 = sum(little_range) / 2
    x2 = x1 - f(x1) / df(x1)
    counter = 1

    while abs(x2 - x1) > epsilon:
        x1 = x2
        x2 = (x1 - f(x1) / df(x1))
        counter += 1

    return x2, counter


def secant_method(pol, little_range, epsilon):
    f = lambdify(x, pol)
    x1, x2 = little_range
    x3 = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))
    counter = 1

    while abs(x3 - x2) > epsilon:
        counter += 1
        x1 = x2
        x2 = x3
        x3 = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))

    return x3, counter


x = sp.symbols('x')
user_func = x**4 + x**3 + -3*x**2
user_range = (-10, 10)
user_epsilon = 0.0001
user_step = 0.1


Drive(user_func, user_range, user_epsilon, user_step)
