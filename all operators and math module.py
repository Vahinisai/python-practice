#Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
import math
a = int(input("enter 1st integer number:"))
b = int(input("enter 2nd integer number:"))
print(F'{a}+{b}={a+b}')
print(F'{a}-{b}={a-b}')
print(F'{a}*{b}={a*b}')
print(F'{a}/{b}={a/b}')
print(F'{a}%{b}={a %b}')
print(F'max({a},{b})={max(a,b)}')
print(F'min({a},{b})={min(a,b)}')
print(F'pow({a},{b})={math.pow(a,b)}')
print(F'sqrt({a})={math.sqrt(a)}')
print(F'fact({a})={math.factorial(a)}')
print(F'gcd({a},{b})={math.gcd(a,b)}') 
