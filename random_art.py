
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


#def create_expression():
    #"""This function takes no arguments and returns an expression that
    #generates a number between -1.0 and 1.0, given x and y coordinates."""
    #expr = lambda x, y: (random.random() * 2) - 1
    #return expr


#def run_expression(expr, x, y):
    #"""This function takes an expression created by create_expression and
    #an x and y value. It runs the expression, passing the x and y values
    #to it and returns a value between -1.0 and 1.0."""
    ##return expr(x, y)

# python create_art.py --color

from math import sin, cos, tan, atan, pi, e, cosh
import random

a = sin
b = cos
c = atan
sin_list = random.choice([a,b,c])
num_list = random.choice([1,2,3,4,5,6,7,1])
xa = random.choice([.2,.55,.432,-.783,-.3958])
ox = random.choice([pi, e])

def tonydelk(x,y):
    return cos(atan(y) * sin_list(x)) * sin(pi * x**2) * cosh(pi*sin(x)*atan(y**3)) * 1 / num_list

def craziness(x,y):
    return tan(sin(y) * cos(x)) * cos(pi * x**2)

def paul_pierce(x,y):
    return atan(cos(sin_list(y**2 + xa** 7)))

def madplayer(x,y):
    return cos(sin_list(y) * sin(x)) * sin(pi * x**num_list) * cosh(pi*sin(x)*atan(y**3))

def tmac(x,y):
    return y / e**(cos(atan(y) * sin(x)) * sin(pi * x**2) * cosh(pi*sin(x)*atan(y**3)) )

def kobe(x,y):
    return x / pi**(cos(atan(y) * sin(x)) * sin(pi * x**2) * cosh(pi*sin(x)*atan(y**3)) )

def shaq(x,y):
    return e*num_list * x**num_list * (x**5 + y**num_list) * cos(sin_list(y) * sin(x)) * sin(pi + x**2) * cosh(pi*sin(x)*atan(y**3)) * x / pi**(cos(atan(y) * sin(x)) * sin(pi * x**2) * cosh(pi*sin(x)*atan(y**3)) )

def motumbo(x,y):
    return pi*num_list * x**num_list * (x**num_list + y**num_list) * y / e**(cos(atan(y) * sin(x)) * sin(pi * x**2) * cosh(pi*sin(x)*atan(y**3)) )

def create_expression():
    expr = random.choice([craziness, paul_pierce, tonydelk, madplayer, tmac, kobe, shaq, motumbo])
    return expr

def run_expression(expr, x, y):
    return expr(x, y)
