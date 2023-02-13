divisor = 1
pi = 0
for i in range(5000):
    if(i%2 == 0):
        pi = pi + 4/divisor
    else:
        pi = pi - 4/divisor
    divisor = divisor + 2
print(pi)

exec




divisor = 1
pi = 0
x = lambda t:t if t%2 == 1 else t*-1
for i in range(5000):
    pi = pi + 4/x(divisor)
    print(x(divisor))
    divisor = divisor + 2
    #print(pi)
print(pi)