fib = [1,2]
while (fib[-1] + fib[-2]) < 4000000:
    fib.append(fib[-2]+fib[-1])

def isEven(n):
    return n % 2 == 0

print(sum(filter(isEven,fib)))
