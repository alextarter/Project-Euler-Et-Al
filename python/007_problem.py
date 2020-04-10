# project euler problem 7
def primes_up_to(n):
    upper_bound = n + 1
    number_list = [True] * upper_bound
    number_list[0] = False
    number_list[1] = False
    
    current_prime = 2
    while current_prime**2 < upper_bound:
        for n in range(current_prime**2, upper_bound, current_prime):
            number_list[n] = False
        current_prime += number_list[current_prime + 1:len(number_list)].index(True) + 1

    primes_list = []
    for i in range(2, upper_bound):
        if number_list[i]:
            primes_list.append(i)

    return primes_list

print(primes_up_to(200000)[10001-1])
# answer: 104743