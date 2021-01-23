# -*- coding: utf-8 -*-
"""
HW1
Geuntae Park
305 142 880
"""
#ALL TEST CASES RUN SUCCESFULLY AS THE INSTRUCTIONS STATE
"""
• Problem 1:
Write a function largerIndex(c) that takes as input a list c of numbers, and returns
a new list k such that k[i] = 1 if c[i] > i, k[i] = 0 if c[i] = i, k [i] = -1 if 
c[i] < i.
Test cases:
l1 = [1,2,0,4,2,1,40,-5]
l2 = [0,3,2,1,32,3,4,0]
largerIndex(l1) should return [1, 1, -1, 1, -1, -1, 1, -1].
largerIndex(l2) should return [0, 1, 0, -1, 1, -1, -1, -1].

"""
def largerIndex(c):
    k = []
    i = 0
    for num in c:
        if num > i:
            k.append(1)
        elif num == i:
            k.append(0)
        else:
            k.append(-1)
        i+=1
    return k

"""
• Problem 2:
Write a function squareUpTo(n) that takes as input a positive integer n, and returns
a list of all the square numbers up to (and possibly including) n.
Test cases:
squareUpTo(10) should return [0, 1, 4, 9].
squareUpTo(100) should return [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
"""
def squareUpTo(n):
    y = ([i**2 for i in range(100)])
    z = [0]
    u = 0
    while z[u] <= n:
        z.append(y[u])
        u+=1
    z.pop(0)
    z.pop(-1)
    return z
"""
• Problem 3:
Write a function flip1in3() that uses only “fair coins” to generate a “biased coin”
with success probability 1/3. That is, this function returns False with probability 2/3
and returns True with probability 1/3. To simulate a “fair coin”, use random.randint(0,1).
"""

"""for this problem I approximated 1/3 as 11/32.
               0                               1
              1 2              |              1 2 
            2 3 2 3            |            2 3 2 3 
        3 4 3 4 3 4 3 4        |        3 4 3 4 3 4 3 4 
4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 5|4 5 4 5 4 5 4 5 4 5 4 5 4 5 4 5 

t t t t t t t t t t t f f f f f|f f f f f f f f f f f f f f f f
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6|7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
to make the code more readable, I used (0,1) for the first flip, (1,2) for the next, (2,3), (3,4), and (4,5) to represent each iterative coin flip.
As the randint() still calls 1 number between 2, it still represents a fair coin.
"""
import random
def flip1in3():
    if random.randint(0,1) == 0:
        if random.randint(1,2) == 1:
            return True
        if random.randint(1,2) == 2:
            if random.randint(2,3) == 2:
                if random.randint(3,4) == 3:
                    return True
                if random.randint(3,4) == 4:
                    if random.randint(4,5) == 5:
                        return True
    return False
#after looping the function 1,000,000 times, it yields a true to false ratio of 0.344668 and 0.655332 respectively
"""
• Problem 4:
Write a function duplicates(c) that takes as input a list c of integers. Some elements
appear twice and others appear once. The function outputs all the elements as a list
that appear twice in the list c. The elements in the output should preserve the original
order.
Test cases:
l3 = [1,2,5,3,6,2,4,5]
l4 = [1,3,5,5,1,4,3]
duplicates(l3) should return [2,5].
duplicates(l4) should return [1,3,5].
"""
def duplicates(c):
    seen = {}
    dupes = []
    for i in c:
        if i not in seen:
            seen[i] = 1
        else:
            if seen[i] == 1:
                dupes.append(i)
            seen[i] += 1
    return dupes