n = 600851475143
c = 2
while n > 1:
    if n % c == 0:
        n /= c
    else:
        c += 1

print(c)
