#Given 5%x = 2, 11%x = 3 and 17%x = 5, find 935%x:
from sympy.ntheory.modular import crt
N = [5,11,17]
A = [2, 3, 5]
a = crt(N,A)
print(a)
