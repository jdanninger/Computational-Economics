#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 6. optimization and consumer theory

In this project, you will be practicing on root finding and optimization problems
In addition, you will apply the computational method to solve the utility
maximization problem in economics.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
from scipy.optimize import minimize

#=============================================================================
# Section 1. Root finding and optimization
#=============================================================================
# 1.1. define the function y = ln(x) + (x-6)^3 - 4x + 30
# you can find the printed equation on Canvas
def f(x):
    return np.log(x) + (x - 6) ** 3 - 4 * x + 30


# 1.2. plot the function on the domain [1, 12]
x = np.linspace(1, 12, 100)
y = f(x)

def plot_function(x, y):

    plt.figure(figsize=(8, 6))  # Optional: set the size of the figure
    plt.plot(x, y, linestyle='-', color='b', label='Data Line')
    plt.title('Plot of x vs. y')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.grid(True)  # Optional: adds a grid
    plt.legend()  # Optional: adds a legend
    plt.show()

plot_function(x, y)


# 1.3. derive and define the first-order derivative of the function
def fp(x):
    return 1/x + 3*(x-6)**2 - 4
    # y = 1/x + 3(x-6)^2 - 4


# 1.4. plot it on the domain [1, 12]

plot_function(x, fp(x))

# 1.5. Define the Newton-Raphson algorithm (as a function)
def newton_raphson(f,fp, initial_guess, tolerance=1e-9 , max_iteration=100):
    """
    This function will apply the Newton-Raphson method to find the root of a given function
    Parameters:
    ------------
    f : function
       The original function we wanted to find roots
    fp : function
        The first order derivative of the original function
    initial_guess: list
        A list of starting points.
    tolerance : float, optional
        defines how close to zero needs to be
    max_iteration : int
        defines maximum iterations if not converge
    Return:
    roots : list
        a list of roots found
    """
    roots = []
    for guess in initial_guess:
        x = guess
        for i in range(max_iteration):
            x1 = x - f(x) / fp(x)
            if abs(x1 - x) < tolerance:
                roots.append(x1)
                break
            x = x1
    return roots



# 1.6.Use the Newton-Raphson algorithm you defined to find the root of the function
# store the result in a list named as res_1

res_1 = newton_raphson(f, fp, [4, 7])

print(res_1)

# 1.7. use the Newton-Raphson method to find the
# maximum value on the domain [4, 8], name the returned variable as res_2
def fpp(x):
    return -1/x**2 + 6*(x-6)


res_2 = newton_raphson(fp, fpp, [4, 8])[0]
print(res_2)

# 1.8. use the Newton-Raphson method to find the
# minimum value on the domain [4, 8], name the returned variable as res_3
res_3 =newton_raphson(fp, fpp, [4, 8])[1]
print(res_3)

# 1.9. use the scipy.optimize library to
# (a). find the root of f(x), store the result in variable res_4
res_4 = root(f, 4)
print(res_4)

# (b). find miniumn value of f(x) on the domain [4, 8],
# name the returned var as res_5
res_5 = minimize(f, 5, bounds=[(4, 8)])
print(res_5)
# (3). find maximum value of f(x) on the domain [4, 8],
# name the returned var as res_6
res_6 = minimize(lambda x: -f(x), 5, bounds=[(4, 8)])
print(res_6)


#=============================================================================
# Section 2. Utility Theory and the Application of Optimization
#=============================================================================

# Consider a utility function over bundles of A (apple) and B (banana)
#  U(B, A) =( B^alpha) * (A^(1-alpha))
# hint: you can find the printed equation on Canvas: project 7.

# 2.1. Define the given utility function
def utility(A, B, alpha):
    return B ** alpha * A ** (1 - alpha)


# 2.2. Set the parameter alpha = 1/3,
# Assume the consumer always consume 1.5 units of B.
# plot the relationship between A (x-axis) and total utility (y-axis)
# set the range of A between 1 and 10
A = np.linspace(1, 10, 100)


def plot_utility(A, u_level):
    B = 1.5
    u_level = utility(A, B, 1/3)
    plt.plot(A, u_level)
    plt.xlabel('A')
    plt.ylabel('U')
    plt.title('Utility function')
    plt.show()

plot_utility(A, 1/3)


# 2.3.  plot the 3-dimensional utility function
# 3-d view of utility
A = np.linspace(1, 10, 100)
B = np.linspace(1, 10, 100)
A, B = np.meshgrid(A, B)
u_level = utility(A, B, 1/3)


def plot_utility_3d(A, B, u_level):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(A, B, u_level, cmap='viridis')
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_zlabel('U')
    plt.show()
plot_utility_3d(A, B, u_level)



# 2.4.plot the utility curve on a "flatten view"
A = np.linspace(1, 10, 100)
B = np.linspace(1, 10, 100)
A, B = np.meshgrid(A, B)
u_level = utility(A, B, 1/3)

def plot_utility_flat(A, B, u_level):
    plt.contourf(A, B, u_level, levels=20)
    plt.colorbar()
    plt.xlabel('A')
    plt.ylabel('B')
    plt.title('Utility function')
    plt.show()


plot_utility_flat(A, B, u_level)

# 2.5. from the given utitlity function, derive A as a function of B, alpha, and U
# plot the indifferences curves for u=1 ,3,5,7,9 on the same figure.
# Put B on the x-axis, and A on the y-axis
def A_indifference(B, ubar, alpha=1/3):
    return (ubar / B ** alpha) ** (1 / (1 - alpha))

def plot_indifference_curves(ax, alpha=1/3):
    B = np.linspace(1, 10, 100)
    for ubar in [1, 3, 5, 7, 9]:
        A = A_indifference(B, ubar, alpha)
        ax.plot(B, A)
    ax.set_xlabel('B')
    ax.set_ylabel('A')
    ax.legend()
    ax.set_title('Indifference Curves')
    plt.show()


fig, ax = plt.subplots()
plot_indifference_curves(ax)


# 2.6.suppose pa = 2, pb = 1, Income W = 20,
# Add the budget constraint to the  previous figure
def A_bc(B, W, pa, pb):
    return (W - pb * B) / pa


def plot_budget_constraint(ax, W, pa, pb):
    B = np.linspace(1, 10, 100)
    A = A_bc(B, W, pa, pb)
    ax.plot(B, A)
    ax.set_xlabel('B')
    ax.set_ylabel('A')
    ax.legend()
    ax.set_title('Budget Constraint')
    plt.show()

fig, ax = plt.subplots()
plot_budget_constraint(ax, 20, 2, 1)


# 2.7. find the optimized consumption bundle and maximized utility
def objective(B, W=20, pa=2, pb=1):
    A = A_bc(B, W, pa, pb)
    return -utility(A, B, 1/3)

optimal_B = minimize(objective, 1, bounds=[(1, 10)]).x
optimal_A = A_bc(optimal_B, 20, 2, 1)
optimal_U = utility(optimal_A, optimal_B, 1/3)


