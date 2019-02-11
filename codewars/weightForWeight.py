def weight(num):
    sum = 0
    while num:
        num, rest = divmod(num, 10)
        sum += rest
        
    return sum

def order_weight(strng):
    nums = [[i, weight(int(i))] for i in strng.split()]
    nums.sort(key = lambda k: (k[1], len(k[0][0]) if len(k[0][0]) == 0 else k[0]))
    return ' '.join([n[0] for n in nums])

print(order_weight("103 123 4444 99 2000"))

