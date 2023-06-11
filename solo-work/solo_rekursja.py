# funkcja sum_list l
# is l empty? y->0 n->l[0]+reszta reszta=sum_list(reszta)

def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_list(list[1:])

print (sum_list([1, 2, 4]))
print (sum_list([]))
print (sum_list([1, 2, 4, 7, 9]))

# funkcja n!
# is n>0?
# yes->none
# no-> n<2?
# yes->1
# no->n*silnia(n-1))

def silnia(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        return n*silnia(n-1)
print (silnia (3))
print (silnia (1))
print (silnia (-1))

#fibonacci
# is n<0?
    # yes->none
# is n=0?
    # yes->0
#is n=1
    #yes->1
# result = (n-1) + (n-2)

def fibonacci(n):
    if n<0:
        return None
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print (fibonacci(0))
print (fibonacci(1))
print (fibonacci(5))
print (fibonacci(10))
print (fibonacci(-1))
