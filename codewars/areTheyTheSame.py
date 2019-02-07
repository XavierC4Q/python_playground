import math

def comp(array1, array2):
    if None == array1 or None == array2:
        return False

    a = sorted(array1)
    b = sorted(array2)

    for n in range(len(a)):
        if math.sqrt(b[n]) != a[n]:
            return False
    return True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a1, a2))