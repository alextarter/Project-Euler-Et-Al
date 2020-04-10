def gcd(s,t):
    if s % t == 0:
        return t
    else:
        return gcd(t, s % t)

# print(gcd(24,108))

def lcm(s,t):
    return s*t//gcd(s,t)

# print(lcm(10,15))

c = 1
# range is inclusive on left, not on right
for i in range(1, 20+1):
    c = lcm(c, i)

print(c)