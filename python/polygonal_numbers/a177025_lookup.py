def polygonal_number(k,n):
    return ((k-2) * n**2 - (k-4) * n)/2

def is_in_row(k, lookup_number):
    n = 2
    while polygonal_number(k,n) < lookup_number:
        n += 1
    if polygonal_number(k,n) == lookup_number:
        return [(k,n)]
    else:
        return []

def count_row_presence(lookup_number):
    counter = []
    for i in range(3, lookup_number):
        counter += is_in_row(i, lookup_number)
    return counter + [(lookup_number,2)]
