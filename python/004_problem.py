productList = []
for i in range(100,1000):
    for j in range(i,1000):
        productList.append(i*j)

def isPalindrome(n):
    nString = str(n)
    return nString == nString[::-1]

print(max(filter(isPalindrome,productList)))
