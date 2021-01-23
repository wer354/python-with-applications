"""
HW1
Geuntae Park
305 142 880
"""

"""
Problem 1:
Write a function longestpath(d) that 
nds the length of the longest path, (a : b) !
(b : c) !    , in a dictionary d. It counts each pointer from a key to a value as one
step. For example, the path (a : b) ! (b : c) has length 2. To avoid cycles, we do not
allow any key to appear more than once in a path (as a key).
Test cases:
d1 = {"a":"b","b":"c"}
d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}
longestpath(d1) should return 2.
longestpath(d2) should return 5.
"""
d1 = {"a":"b","b":"c"}
d2 = {"a":"b","b":"c","c":"d","e":"a","f":"a","d":"b"}

def lengthOfPath(first, d):
    #creates a visited keys list with first key listed
    visited = [first]
    current = first
    #loop goes through keys
    while current in d.keys():
        current = d[current]
        #this breaks the loop if a key is repeated or terminates
        if current in visited or current not in d.keys(): break
        #adds currently seen value to visited list
        visited.append(current)
    #returns length of the loop
    return len(visited)

def longestPath(d):
    #creates list of path lengths, iterates lengthOfPath for all dict keys
    pathLengths = []
    for first in d.keys():
        length = lengthOfPath(first,d)
        pathLengths.append(length)
    #returns the longest by selecting the maximum value from pathLengths list
    return max(pathLengths)

"""
Problem 2:
Implement Newton's method (also known as the Newton-Raphson method) to find a
root (zero) of a function. No prior knowledge of this algorithm is needed. Just follow
the steps.
Given a function f(x) , the function's derivative f0(x), and a desired tolerance  
(usuallya very small positive number), your goal is to find a desired value x which
is close enough to a root of f(x) such that |f(x*)| <= .

Write your algorithm in a solve function that takes as input a function f(x),
its derivative f0(x), an initial guess x0 and the tolerance . This function can be
called like this: solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
"""
"""
TEST CASES
x**2-1,2*x,3
x**2-1,2*x,-1
exp(x)-1,exp(x),1
sin(x),cos(x),0.5

1.0000305180437934
-1
1.5641107898984284e-06
3.311802132639069e-05
"""
import math
#imported math for solving exp, sin, cos test cases

def solve(f, x, eps):
    while(abs(f(x)[0]) > eps):
        x -= (f(x)[0] / f(x)[1])
    return x
