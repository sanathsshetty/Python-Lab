def eGCD(a, b):
    if b == 0:
        return a
    else:
        return eGCD(b, a%b)
    
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
result = eGCD(a, b)
print('The GCD is', result)
