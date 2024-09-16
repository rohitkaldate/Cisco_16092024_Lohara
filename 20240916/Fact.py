def find_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

f1 = find_fact(5) #120
#f2 = find_fact(4) #24
print(f1)
#print(f2)