PMT = float(input("enter payment contributed amount: "))
R = float(input("enter rate amount: "))
n = float(input("enter number of times amount: "))
T = float(input("enter time amount: "))

A = PMT * ([(1+R/n)**n*T - 1]/(R/n))

print(A)