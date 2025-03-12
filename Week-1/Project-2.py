P = float(input("enter principle amount: "))
R = float(input("enter rate amount: "))
n = float(input("enter number of times amount: "))
T = float(input("enter time amount: "))

A = P*(1+R/n)**n*T

print(A)