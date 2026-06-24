import sympy
from sympy import symbols, sympify
from sympy.solvers import solve

x, y = symbols('x, y')
eq1 = sympify(input('Enter first equation: 0 = '))
eq2 = sympify(input('Enter Second equation: 0 = '))

factored_eq1 = sympy.factor(eq1)
factored_eq2 = sympy.factor(eq2)

solution = solve([eq1, eq2], (x, y))
print('The factoredeq1 solution is: ', factored_eq1)
print('The factoredeq2 solution  is: ',  factored_eq2)
print('The answer is: ', solution)


    
    
    
    
    
    